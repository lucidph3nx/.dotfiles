#!/bin/sh
session="jarden-ssh"

# also take the opportinity to change kube configs
export KUBECONFIG=/home/ben/.config/kube/config-work

tmux new-session -d -s $session
tmux rename-window -t $session:0 "uat-18w"
tmux send-keys -t $session:0 "ssh uat-18w" C-m
tmux new-window -t $session:1 -n "prod-18w"
tmux send-keys -t $session:1 "ssh prod-18w" C-m
tmux new-window -t $session:2 -n "prod-18a"
tmux send-keys -t $session:2 "ssh prod-18a" C-m
tmux new-window -t $session:3 -n "uat-s1t"
tmux send-keys -t $session:3 "ssh uat-s1t" C-m
tmux new-window -t $session:4 -n "prod-s1t"
tmux send-keys -t $session:4 "ssh prod-s1t" C-m

tmux attach-session -t $session
