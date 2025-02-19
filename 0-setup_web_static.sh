#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static 

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create fake index.html file for testing
sudo touch /data/web_static/releases/test/index.html
echo "<html><body>Testing Nginx configuration</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link to current release
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '38i\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0