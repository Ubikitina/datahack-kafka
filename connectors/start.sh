#!/bin/bash

echo "Launching Kafka Connect worker"
/etc/confluent/docker/run & 

# Sleep for 120 seconds
echo "Waiting for Kafka Connect to start listening on localhost ⏳"
sleep 120

echo "Creating SpoolDirCsvSourceConnector connector"
curl -d @"./connect-file-source.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors

echo "Creating MongoSinkConnector connector"
curl -d @"connect-mongo-sink.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors

sleep infinity