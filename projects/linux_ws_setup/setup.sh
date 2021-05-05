#!/bin/bash

sudo apt update
sudo apt upgrade

# Install C compilers
sudo apt install build-essential

# Install Ruby and bundler
sudo apt install software-properties-common
sudo apt-add-repository -y ppa:rael-gc/rvm
sudo apt update
sudo apt install rvm
sudo -s
source /etc/profile.d/rvm.sh
rvm install 2.7
rvm use 2.7
# Check with ruby --version

# Install Flutter
wget https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_2.0.6-stable.tar.xz

# Instsall Node.js
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install nodejs
