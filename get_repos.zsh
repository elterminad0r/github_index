#!/usr/bin/env zsh
wget -qO- "https://api.github.com/users/goedel-gang/repos?page=$1"
