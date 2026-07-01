#!/bin/bash


# user creator

echo "*** create user ***"
read -p "Pick a number for typr of user [ADMIN: 1 , Normal : 2]  : " type
read -p "Enter the username : " username

sudo adduser $username

if [ "$type" = "1" ]; then
    sudo usermod -aG "$username"
fi

echo "ceated sucessfully !!!"


#install Nginx

echo "updating system ..."
sudo apt update -y
echo "installing Nginx..."
sudo apt install nginx -y 


#firewall
sudo apt install ufw -y 

sudo ufw allow 80