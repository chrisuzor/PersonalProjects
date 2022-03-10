#!/bin/bash
docker stats --no-stream > /tmp/memory.log

sed -i 's/CONTAINER//g' /tmp/memory.log

conatiners=$(awk '{if(NR>1 && $7>0.02) print $2}' /tmp/memory.log)

echo containers