import requests


def main():
    tag_name = requests.get(
        'https://api.github.com/repos/microsoft/vscode/releases/latest').json()['tag_name']

    r = requests.get(
        f'https://api.github.com/repos/microsoft/vscode/git/ref/tags/{tag_name}').json()

    sha = r['object']['sha']

    sha_type = r['object']['type']

    # if sha_type != 'commit':
        

    print(tag_name, sha, sha_type)
    print(f'https://update.code.visualstudio.com/commit:{sha}/server-linux-x64/stable')


    # 'https://api.github.com/repos/microsoft/vscode/git/tags/${sha}'


if __name__ == '__main__':
    main()
