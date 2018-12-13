#!/bin/bash
sudo apt-get install tmux python-pip git -y &> /dev/null
pip install requests &> /dev/null
mkdir gitdir/
cd gitdir/
git clone https://github.com/bab2501/beerdrinker.git
cd beerdrinker/
sudo chmod 777 ~/gitdir/beerdrinker
sudo chmod 777 ~/gitdir/beerdrinker/*
