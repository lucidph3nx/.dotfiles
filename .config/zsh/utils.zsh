# a place to install various utils, mostly version managers

# adds cargo binaries to path
export PATH="${PATH}:${HOME}/.local/share/cargo/bin"

# adds krew k8s package manager to path
# krew (kubectl package manager)
export PATH="${PATH}:${HOME}/.krew/bin"

# add python binaries to PATH
export PATH="${PATH}:${HOME}/.local/share/python/bin"

# mise version manager - hopefully the last I'll ever need
# eval "$(mise activate zsh)"
. /opt/asdf-vm/asdf.sh

# direnv env vars by directory
eval "$(direnv hook zsh)"

# os specific utils
# if [[ "$OSTYPE" == "darwin"* ]]; then
#   # metals and other stuff installed via courser
#   if [ ! -d "${HOME}/.local/share/coursier/bin" ]; then
#     # symlink because of space in Application Support folder
#     mkdir -p "${HOME}/.local/share/coursier"
#     ln -s "${HOME}/Library/Application Support/Coursier/bin" "${HOME}/.local/share/coursier"
#   fi
#   export PATH="${PATH}:${HOME}/.local/share/coursier/bin"
# elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
#   export PATH="${PATH}:${HOME}/.local/share/coursier/bin"
# fi
