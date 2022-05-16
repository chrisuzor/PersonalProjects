#!/bin/bash

containers=$(docker ps -a | awk '{if(NR>1) print $0}')
IFS='
'
status="Up"
for container in $containers
do
  if echo "$container" | grep -q "$status"; then
  echo "Container is Running : $container";
else
  echo "Restarting this container" : $container
  IFS=' ' read -r -a array <<< "$container"
  docker restart "${array[@]: -1:1}"
fi
done
