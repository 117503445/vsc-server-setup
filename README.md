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

Although VS Code can automate this process, this project provides a script for manually installing VS Code Server when creating Docker images for development environments. In addition, the poor network environment in China often makes downloading VS Code Server unsuccessful, so this project provides an image of the VS Code Server binary package based on AliCloud OSS to speed up the download and installation for Chinese users.

## Getting Started

```sh
# Officially download and install the latest VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/install-lastest-vsc.sh | bash

# China Source Download and install the latest VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/cn/install-lastest-vsc.sh | bash
```

## Usage

The following is an example of the official source

### Regular updates

`EDITOR=nano crontab -e`

type `0 * * * * curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/cn/install-lastest-vsc.sh | bash`

The latest VS Code Server can be downloaded and installed automatically (every hour).

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

- [b01](https://gist.github.com/b01/0a16b6645ab7921b0910603dfb85e4fb) provides the original download script

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
