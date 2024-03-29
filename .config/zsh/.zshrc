# for when you want to debug zsh startup (also uncomment zprof below)
# zmodload zsh/zprof

# XDG Environment Variable load First!
source $HOME/.config/zsh/xdg.zsh
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# add to path
eval export PATH="${PATH}:$HOME/.local/scripts/"
eval export PATH="${PATH}:$HOME/.local/bin/"

# source brew if on macos
if [[ "$OSTYPE" == "darwin"* ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# ENVS
# --- Environment Variables
source $XDG_CONFIG_HOME/zsh/env.zsh
# --- Aliases
source $XDG_CONFIG_HOME/zsh/aliases.zsh
# --- Secrets
source $XDG_CONFIG_HOME/zsh/secrets.zsh
# oh-my-zsh config
source $XDG_CONFIG_HOME/zsh/omz.zsh
source $XDG_CONFIG_HOME/zsh/p10k.zsh

# --- utils
source $XDG_CONFIG_HOME/zsh/utils.zsh

# --- key mappings - load last 
source $XDG_CONFIG_HOME/zsh/mappings.zsh

# for when you want to debug zsh startup
# zprof
