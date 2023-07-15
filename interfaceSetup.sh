#!/bin/bash
# Working from Ubuntu 22* 
# Setup is based on Supabase's free tier option
# Calling primary from homeserver restricts Grafana data limited to time dependent updates in raw text form
# consider changing host!

# Install Grafana
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install -y grafana

# Start Grafana service
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

# Install SQLite data source plugin for Grafana
sudo grafana-cli plugins install grafana-sqlite-datasource

# Restart Grafana service
sudo systemctl restart grafana-server

# Set up SQLite data source in Grafana
# Note: Replace <database_path> with the path to your SQLite database file
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "SQLite",
  "type": "sqlite",
  "access": "proxy",
  "url": "file://<database_path>",
  "database": "",
  "basicAuth": false,
  "isDefault": true
}' http://admin:admin@localhost:3000/api/datasources

# Open Grafana in the default browser
xdg-open http://localhost:3000
