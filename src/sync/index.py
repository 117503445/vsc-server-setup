# -*- coding: utf-8 -*-
import logging
import json

import requests
import fc2


def handler(event, context):
    logger = logging.getLogger()

    tag_name = requests.get(
        'https://api.github.com/repos/microsoft/vscode/releases/latest').json()['tag_name']

    r = requests.get(
        f'https://api.github.com/repos/microsoft/vscode/git/ref/tags/{tag_name}').json()

    sha = r['object']['sha']

    sha_type = r['object']['type']

    # if sha_type != 'commit':
        
    bin_url = f'https://update.code.visualstudio.com/commit:{sha}/server-linux-x64/stable'

    cur_sha = requests.get('https://vsc-server-setup.oss-cn-hangzhou.aliyuncs.com/latest-sha.txt').text

    logger.info(tag_name)
    logger.info(sha)
    logger.info(sha_type)
    logger.info(bin_url)
    logger.info(cur_sha)
    
    if sha == cur_sha:
        return

    import oss2
    auth = oss2.StsAuth(context.credentials.access_key_id, context.credentials.access_key_secret, context.credentials.security_token)
    bucket = oss2.Bucket(auth, 'oss-cn-hangzhou-internal.aliyuncs.com', 'vsc-server-setup')


    logger.info("putting bin")
    bucket.put_object(f'{sha}.tar.gz', requests.get(bin_url))

    logger.info("putting sha")
    bucket.put_object('latest-sha.txt', sha)