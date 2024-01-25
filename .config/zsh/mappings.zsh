# Ctrl-f open tmux-sessionizer
bindkey -s ^f "cli.tmux.projectSessioniser\n"
bindkey -s ^s "cli.tmux.sshHostSessioniser\n"
# Ctrl-k open k9s
bindkey -s ^k "k9s --headless\n"
# Ctrl-v open nvim in current directory
bindkey -s ^v "nvim\n"
# Ctrl-p open python
bindkey -s ^p "python\n"

# Ctrl-z to run zscaler script
bindkey -s ^z "cd ~/code/zscaler-automatic-login && poetry run python main.py\n"
