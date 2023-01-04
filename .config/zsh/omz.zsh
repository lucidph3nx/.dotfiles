# file to configure oh-my-zsh

# Path to your oh-my-zsh installation.
export ZSH="$XDG_CONFIG_HOME/zsh/oh-my-zsh"

# set theme
#ZSH_THEME="robbyrussell"
ZSH_THEME="powerlevel10k/powerlevel10k"

zstyle ':omz:update' mode auto      # update automatically without asking

# plugins to enable
plugins=(
	git
  git-auto-fetch
  history
	kubectl
	asdf
  vi-mode
)

# source
source $ZSH/oh-my-zsh.sh
