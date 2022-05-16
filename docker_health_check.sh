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
<<<<<<< HEAD
done
=======
done
>>>>>>> 94a81eb432a52582e503668e85b4cc9249584108
