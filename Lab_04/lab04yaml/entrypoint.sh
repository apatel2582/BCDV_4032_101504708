#!/bin/bash

# Start MongoDB without forking, with the specified arguments
mongod --bind_ip_all --logpath /var/log/mongodb.log &

# Wait for MongoDB to start
sleep 10

# Run the init script
mongosh /data/db/mongo-init.js

# Wait for mongod process
wait
