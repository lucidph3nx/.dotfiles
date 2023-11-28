# --- Aliases ---

# preserve env when using sudo
alias sudo='sudo -E -s'

# exa instead of ls
alias ls='exa'
alias l='exa -la'
alias tree='exa --tree -la'

# bat instead of cat
# alias cat='bat'

# ripgrep instead of grep
alias grep='rg'

#nvim
alias {v,vim}=nvim

# .dotfiles git alias
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
alias dotfiles-private='/usr/bin/git --git-dir=$HOME/.dotfiles-private --work-tree=$HOME'

alias ds='dotfiles status'
alias da='dotfiles add'
alias dc='dotfiles commit'
alias dd='dotfiles diff'
alias dr='dotfiles restore'
alias dp='dotfiles push'
alias dP='dotfiles pull --rebase'


# kubectl in a docker container for legacy jarden on prem k8s
alias kop="~/code/dev-tools/kubectl-1.3.7-docker/kubectl.sh"

# youtube download script for music
alias ytm-download="yt-dlp  --add-metadata --format m4a --youtube-skip-dash-manifest -i -o '~/music/%(artist)s/%(album)s/%(title)s.%(ext)s' --sponsorblock-remove 'music_offtopic'"

# for sshing into things that don't know kitty
alias ssh='TERM=xterm-color ssh'

# sbt (XDG Compliance)
alias sbt=sbt -ivy "$XDG_DATA_HOME"/ivy2 -sbt-dir "$XDG_DATA_HOME"/sbt
# yarn (XDG Compliance)
alias yarn='yarn --use-yarnrc "$XDG_CONFIG_HOME/yarn/config"'
# wget (XDG Compliance)
alias wget=wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"

# terminal calculator
alias c=calc
# better terminal calc
alias py=python

alias neofetch=neowofetch

alias cilium=cilium-cli
