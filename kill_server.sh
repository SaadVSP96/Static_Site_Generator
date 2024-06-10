#!/bin/bash

# Check if a port number was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <port>"
  exit 1
fi

PORT=$1

# Find the PID of the process using the specified port
PID=$(lsof -t -i:$PORT)

# Check if a PID was found
if [ -z "$PID" ]; then
  echo "No process found using port $PORT"
  exit 1
fi

# Kill the process using the specified port
echo "Killing process $PID using port $PORT"
kill -9 $PID

# Check if the process was successfully killed
if [ $? -eq 0 ]; then
  echo "Process $PID has been killed successfully"
else
  echo "Failed to kill process $PID"
fi
