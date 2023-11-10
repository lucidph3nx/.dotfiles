#!/bin/bash

width=$(swaymsg -t get_outputs | jq '.[0].rect.width' | xargs printf "%.0f\n")

# Check if running in super-ultrawide
if [ $width -gt 5000 ]; then
  swaymsg smart_gaps inverse_outer
  swaymsg gaps horizontal $(($width/4))
  swaymsg gaps horizontal all set $(($width/4))
fi
