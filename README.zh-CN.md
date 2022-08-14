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

在远程系统中需要安装最新版本的 VS Code Server。尽管 VS Code 可以自动完成此过程，但是在制作用于开发环境的 Docker 镜像时，还是需要本项目提供的手动安装 VS Code Server 的脚本。此外，中国糟糕的网络环境使下载 VS Code Server 经常失败，本项目基于 阿里云 OSS 提供了 VS Code Server 二进制包的镜像，从而加速中国用户的下载安装。

## 快速开始

```sh
# 官方下载安装最新的 VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/install-lastest-vsc.sh | bash

# 中国源下载安装最新的 VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/cn/install-lastest-vsc.sh | bash
```

## 使用方法

以下以中国源为例

### 定时检查更新

`EDITOR=vim crontab -e`

输入 `0 * * * * curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/cn/install-lastest-vsc.sh | bash`

即可自动（每小时）下载安装最新的 VS Code Server

<!-- LICENSE -->
## License

在 MIT 许可下发布。更多信息见 `LICENSE.txt`。

<!-- ACKNOWLEDGMENTS -->
## 致谢

- [b01](https://gist.github.com/b01/0a16b6645ab7921b0910603dfb85e4fb) 的原始下载脚本


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
