#!/bin/bash

dir="${HOME}/diary"

# test_command (exists)
if [ ! -d "$dir" ]; then
  mkdir "$dir"
fi

vi "${dir}/$(date '+%Y-%m-%d').txt"
