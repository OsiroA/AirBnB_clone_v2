#!/usr/bin/env bash
# This script configures a web server to host a static website.

# Update the package repository
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Create necessary directory structure
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create an HTML file with content
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link for the current version
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of directories
sudo chown -R ubuntu:ubuntu /data

# Configure Nginx to serve static content
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
/etc/init.d/nginx restart
