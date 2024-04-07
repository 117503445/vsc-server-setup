<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[English README](https://github.com/117503445/vsc-server-setup)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/117503445/vsc-server-setup">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">vsc-server-setup</h3>
  <p align="center">安装最新版本的 VSCode Server
</div>

<!-- ABOUT THE PROJECT -->
## 关于项目

VSCode Remote 允许用户在远程服务器和容器中进行开发，其架构如下图所示。

![architecture](https://code.visualstudio.com/assets/docs/remote/remote-overview/architecture.png)

在远程系统中需要安装最新版本的 VS Code Server。尽管 VS Code 可以自动完成此过程，但是中国糟糕的网络环境使下载 VS Code Server 经常失败。通过本项目，可以使服务器的 VS Code Server 始终保持最新的版本。

## 使用方法

下载 `docker-compose.yml`

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

编写 `./config/config.json`

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
        },
        {
            "type": "s3",
            "endpoint_url": "",
            "ak": "",
            "sk": "",
            "region": "",
            "bucket": "",
        }
    ]
}
```

执行 `docker compose up` 即可进行 VSC Server 的更新

也可以通过 crontab 定期执行此命令

`0 * * * * cd ~/.docker/vsc-server-setup && docker compose up`

<!-- LICENSE -->
## License

在 MIT 许可下发布。更多信息见 `LICENSE.txt`。

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

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
