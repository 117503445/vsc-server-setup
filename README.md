<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[中文 README](https://github.com/117503445/vsc-server-setup/blob/master/README.zh-CN.md)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/117503445/vsc-server-setup">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">vsc-server-setup</h3>

  <p align="center">
    Automatically install the latest version of VSCode Server
</div>

## About The Project

VSCode Remote allows users to develop in remote servers and containers with the architecture shown in the figure below.

![architecture](https://code.visualstudio.com/assets/docs/remote/remote-overview/architecture.png)

You need to install the latest version of VS Code Server on a remote system, and although VS Code can do this automatically, poor network conditions in China often make downloading VS Code Server fail. This project allows you to keep the server's VS Code Server up to date.
## Usage

Download docker-compose.yml

```yaml
version: "3.9"

services:
  vsc-server-setup:
    image: 117503445/vsc-server-setup
    container_name: vsc-server-setup
    volumes:
      - ./config/config.json:/root/config.json:ro
      - ./data:/root/data

      - ~/.ssh:/root/.ssh:ro
      
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
```

Write `./config/config.json`

```json
{
    "logging_level": "INFO",
    "targets": [
        {
            "type": "ssh",
            "name": "server1",

            "host": "127.0.0.1",
            "port": 22,
            "user": "root"
        },
        {
            "type": "ssh",
            "name": "server2",

            "host": "192.168.1.1",
            "port": 22,
            "user": "root"
        }
    ]
}
```

Currently, only SSH method is supported

Execute `docker compose up` to update VSC Server

You can also run this command periodically via crontab

`0 * * * * * cd ~/.docker/vsc-server-setup && docker compose up`

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

[contributors-shield]: https://img.shields.io/github/contributors/117503445/vsc-server-setup.svg?style=for-the-badge
[contributors-url]: https://github.com/117503445/vsc-server-setup/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/117503445/vsc-server-setup.svg?style=for-the-badge
[forks-url]: https://github.com/117503445/vsc-server-setup/network/members
[stars-shield]: https://img.shields.io/github/stars/117503445/vsc-server-setup.svg?style=for-the-badge
[stars-url]: https://github.com/117503445/vsc-server-setup/stargazers
[issues-shield]: https://img.shields.io/github/issues/117503445/vsc-server-setup.svg?style=for-the-badge
[issues-url]: https://github.com/117503445/vsc-server-setup/issues
[license-shield]: https://img.shields.io/github/license/117503445/vsc-server-setup.svg?style=for-the-badge
[license-url]: https://github.com/117503445/vsc-server-setup/blob/master/LICENSE.txt
