#!/usr/bin/bash

# OPC.1: INSTALLING MYSQL USING APT REPOSITORY

mkdir install_mysql

cd install_mysql

#download mysqkl from oficial page

wget https://dev.mysql.com/get/mysql-apt-config_0.8.16-1_all.deb

#install the dwonloaded release package

sudo dpkg -i mysql-apt-config_0.8.16-1_all.deb

#update package information from the mysql apt repository

sudo apt-get update

#installing mysql-server pakage from MYSQL APT repository

sudo apt-get install mysql-server

# at this point, we alredy have MYSQL APT repository on system repository list. we will install other mysql components
# sudo apt-get install pakage-name

# for remove

# sudo apt-get remove mysql-server
# sudo apt-get autoremove

# to uninstall other components use the following commands sudo apt-get remove package-name

# to see a list of packages you have installed from the MYSQL APT repository, type:
dpkg -i | grep mysql | grepii

#or
dpkg --get-selections | grep -v 'deinstall' | more

#type sudo apt-get purge pakage name-package name

# erase config files
sudo rm -rf /etc/mysql/var/lib/mysql
sudo apt-get autoremove
sudo apt-get autoclean
