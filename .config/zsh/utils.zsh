# a place to install various utils, mostly version managers

# rtx version manager - hopefully the last I'll ever need
eval "$(/usr/bin/rtx activate zsh)"

# adds cargo binaries to path
export PATH="${PATH}:${HOME}/.local/share/cargo/bin"

# adds krew k8s package manager to path
# krew (kubectl package manager)
export PATH="${PATH}:${HOME}/.krew/bin"

# add python binaries to PATH
export PATH="${PATH}:${HOME}/.local/share/python/bin"
