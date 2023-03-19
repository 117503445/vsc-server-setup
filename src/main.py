from htutil import file
from pathlib import Path
import logging
import requests
import paramiko

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG)

cfg = file.read_json('config.json')
# logging.info('host %s', cfg[''])

s = requests.session()

dir_data = Path('data')
if not dir_data.exists():
    dir_data.mkdir()

if 'sha' in cfg:
    sha = cfg['sha']
else:
    tag_name = s.get(
        'https://api.github.com/repos/microsoft/vscode/releases/latest').json()['tag_name']
    sha = s.get(
        f'https://api.github.com/repos/microsoft/vscode/git/ref/tags/{tag_name}').json()['object']['sha']

bin_url = f'https://update.code.visualstudio.com/commit:{sha}/server-linux-x64/stable'
logging.debug(f'bin_url = {bin_url}')

file_dest = dir_data / f'{sha}.tar.gz'
if not file_dest.exists():
    # clean old files
    for f in dir_data.glob('*.tar.gz'):
        if f.is_file():
            f.unlink()

    logging.debug(f'downloading {bin_url}')
    r = s.get(bin_url)
    with open(file_dest, 'wb') as f:
        f.write(r.content)

for target in cfg['targets']:
    logging.debug(f'target = {target}')
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(target['host'], username=target['user'])

    _, _stdout, _ = client.exec_command(f"[-d ~/.vscode-server/bin/{sha}]")
    print(_stdout.read().decode())
    client.close()
