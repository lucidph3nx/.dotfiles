# History file
export HISTFILE="$XDG_STATE_HOME"/zsh/history

# editor
export EDITOR=nvim
# oh-my-zsh
# Path to your oh-my-zsh installation.
export ZSH="$XDG_CONFIG_HOME/zsh/oh-my-zsh"

#ZSH_THEME="robbyrussell"
ZSH_THEME="powerlevel10k/powerlevel10k"

# pfetch
export PF_INFO="ascii title os kernel pkgs wm shell editor"

# kubernetes
export KUBECONFIG=/home/ben/.config/kube/config-home
# export KUBECONFIG=/home/ben/.config/kube/config-work

# bun
export BUN_INSTALL="$HOME/.bun" 
export PATH="$BUN_INSTALL/bin:$PATH" 
