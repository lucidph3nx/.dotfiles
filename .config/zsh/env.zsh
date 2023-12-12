# History file
export HISTFILE="$XDG_STATE_HOME"/zsh/history

# editor
export EDITOR=nvim
# oh-my-zsh
# Path to your oh-my-zsh installation.
export ZSH="$XDG_CONFIG_HOME/zsh/oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

# pfetch
export PF_INFO="ascii title os kernel pkgs wm shell editor"

# kubernetes, with host defaults
if [[ "$OSTYPE" == "darwin"* ]]; then
  export KUBECONFIG=/home/ben/.config/kube/config-work
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  export KUBECONFIG=/home/ben/.config/kube/config-home
fi

# I put this here for macports, but it looks generic?
export PATH=/opt/local/bin:/opt/local/sbin:$PATH

