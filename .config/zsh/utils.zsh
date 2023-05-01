# a place to install various utils, mostly version managers

# for node version managers
# assumes brew use on macos
if [[ "$OSTYPE" == "darwin"* ]]; then
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
  source /usr/share/nvm/init-nvm.sh
fi


# adds krew k8s package manager to path
# krew (kubectl package manager)
export PATH="${PATH}:${HOME}/.krew/bin"

# --- jenv - java version manager
# eval export PATH="/home/ben/.jenv/shims:${PATH}"
# export JENV_SHELL=zsh
# export JENV_LOADED=1
# unset JAVA_HOME
# unset JDK_HOME
# jenv rehash 2>/dev/null
# jenv refresh-plugins
# jenv() {
#   type typeset &> /dev/null && typeset command
#   command="$1"
#   if [ "$#" -gt 0 ]; then
#     shift
#   fi
# 
#   case "$command" in
#   enable-plugin|rehash|shell|shell-options)
#     eval `jenv "sh-$command" "$@"`;;
#   *)
#     command jenv "$command" "$@";;
#   esac
# }
