set -e

commit_sha=$(curl --silent https://vsc-server-setup.oss-cn-hangzhou.aliyuncs.com/latest-sha.txt)
bin_dir="$HOME/.vscode-server/bin/${commit_sha}"

# dir already exists, exit.
[ -d "${bin_dir}" ] && exit 0

echo ${commit_sha}
mkdir -pv ~/.vscode-server/bin/"${commit_sha}"

curl -L "https://vsc-server-setup.oss-cn-hangzhou.aliyuncs.com/${commit_sha}.tar.gz" -o "/tmp/vscode-server-linux-x64.tar.gz"

tar --no-same-owner -xzv --strip-components=1 -C ~/.vscode-server/bin/"${commit_sha}" -f "/tmp/vscode-server-linux-x64.tar.gz"