#!/usr/bin/env bash


# prints  start message
echo -e "\e[1;32m START\e[0m"

# update packages
echo -e "\e[1;32m Updating packages\e[0m"
sudo apt-get -y update
echo -e "\e[1;32m Packages updated\e[0m"

# checks if Nginx is installed
if [ -x "$(command -v nginx)" ]; then
            echo -e "\e[1;32m Nginx is already installed\e[0m"
    else
                # Install Nginx
                    echo -e "\e[1;32m Installing Nginx\e[0m"
                        sudo apt-get -y install nginx
                            echo -e "\e[1;32m Nginx installed\e[0m"
fi

# configure firewall
echo -e "\e[1;32m Configuring firewall\e[0m"
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Firewall configured to allow incoming NGINX HTTP connections\e[0m"

# create directories
echo -e "\e[1;32m Creating directories\e[0m"
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;32m Directories created\e[0m"

# add  test string to index.html
echo -e "\e[1;32m Adding test string to index.html\e[0m"
echo "<h1>Welcome to www.codetones.tech</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test string added to index.html\e[0m"

# prevents overwriting current directory
if [ -d "/data/web_static/current" ];
then
            echo -e "\e[1;32m Preventing overwrite of current directory\e[0m"
                sudo rm -rf /data/web_static/current;
fi;

# Creates symbolic link
echo -e "\e[1;32m Creating symbolic link\e[0m"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

# configure Nginx to serve static files
echo -e "\e[1;32m Configuring Nginx to serve static files\e[0m"
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;32m Nginx configured to serve static files\e[0m"

# restart nginx
echo -e "\e[1;32m Restarting Nginx\e[0m"
sudo service nginx restart
echo -e "\e[1;32m Nginx restarted\e[0m"
