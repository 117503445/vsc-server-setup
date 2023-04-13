from htutil import file
from pathlib import Path
import logging
import requests
import paramiko
import paramiko.client
cfg = file.read_json('config.json')
if cfg['logging_level']:
    level = logging._nameToLevel[cfg['logging_level']]
else:
    level = logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(level)

stream_handler = logging.StreamHandler()

formatter = logging.Formatter(
    '%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

# logger.info('host %s', cfg[''])

s = requests.session()

dir_data = Path('data')
if not dir_data.exists():
    dir_data.mkdir()

if 'sha' in cfg:
    sha = cfg['sha']
else:
    tag_name = s.get(
        'https://api.github.com/repos/microsoft/vscode/releases/latest').json()['tag_name']
    logger.info(f'tag_name = {tag_name}')
    tag_url = s.get(
        f'https://api.github.com/repos/microsoft/vscode/git/ref/tags/{tag_name}').json()['object']['url']
    sha = s.get(tag_url).json()['object']['sha']

bin_url = f'https://update.code.visualstudio.com/commit:{sha}/server-linux-x64/stable'
logger.info(f'bin_url = {bin_url}')

file_dest = dir_data / f'{sha}.tar.gz'
if not file_dest.exists():
    # clean old files
    for f in dir_data.glob('*.tar.gz'):
        if f.is_file():
            f.unlink()

    logger.info(f'downloading {bin_url}')
    r = s.get(bin_url)
    if r.status_code != 200:
        logger.error(f'download failed, status_code = {r.status_code}')
        exit(1)
    with open(file_dest, 'wb') as f:
        f.write(r.content)

logger.info('processing targets')

for target in cfg['targets']:
    logger.info(f'target = {target}')
    client: paramiko.client.SSHClient = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    username = target['user']
    client.connect(target['host'], username=username)

    if username == 'root':
        home_dir = '/root'
    else:
        home_dir = f'/home/{username}'
    
    ftp_client = client.open_sftp()
    is_exist = False
    try:
        ftp_client.stat(f'{home_dir}/.vscode-server/bin/{sha}/node')
        is_exist = True
    except IOError as ex:
        logger.debug(ex)
        pass

    logger.info(f'is_exist = {is_exist}')

    if not is_exist:
        ftp_client.put(file_dest, '/tmp/vscode-server-linux-x64.tar.gz')
        command = f'rm -rf ~/.vscode-server/bin/{sha} && mkdir -p ~/.vscode-server/bin/{sha} && echo extra to ~/.vscode-server/bin/{sha} && tar --no-same-owner -zx --strip-components=1 -C ~/.vscode-server/bin/{sha} -f "/tmp/vscode-server-linux-x64.tar.gz"'
        logger.info(f'exec command: {command}')
        _, _stdout, _ = client.exec_command(command)
        logger.info(f'output: {_stdout.read().decode()}')
        
    ftp_client.close()
    # _, _stdout, _ = client.exec_command(command)
    # print(_stdout.read().decode())
    client.close()
