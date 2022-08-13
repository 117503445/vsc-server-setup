<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/117503445/vsc-server-setup">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">vsc-server-setup</h3>
  <p align="center">安装最新版本的 VSCode Server
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## 关于项目

VSCode Remote 允许用户在远程服务器和容器中进行开发，其架构如下图所示。

![architecture](https://code.visualstudio.com/assets/docs/remote/remote-overview/architecture.png)

在远程系统中需要安装最新版本的 VS Code Server。尽管 VS Code 可以自动完成此过程，但是在制作用于开发环境的 Docker 镜像时，还是需要本项目提供的手动安装 VS Code Server 的脚本。此外，中国糟糕的网络环境使下载 VS Code Server 经常失败，本项目基于 阿里云 OSS 提供了 VS Code Server 二进制包的镜像，从而加速中国用户的下载安装。

## 使用方法

```sh
# 官方下载安装最新的 VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/install-lastest-vsc.sh | bash

# 中国源下载安装最新的 VS Code Server
curl -fsSL https://raw.githubusercontent.com/117503445/vsc-server-setup/master/src/fetch/cn/install-lastest-vsc.sh | bash
```

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
[product-screenshot]: images/screenshot.png
[next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[next-url]: https://nextjs.org/
[react.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[react-url]: https://reactjs.org/
[vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[vue-url]: https://vuejs.org/
[angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[angular-url]: https://angular.io/
[svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[svelte-url]: https://svelte.dev/
[laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[laravel-url]: https://laravel.com
[bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[bootstrap-url]: https://getbootstrap.com
[jquery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[jquery-url]: https://jquery.com
