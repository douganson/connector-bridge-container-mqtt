#!/bin/sh

rm -f ./logs/*.log 2> /dev/null
mkdir -p ./logs
java -Dmax-thread-pool-size=30 -Dconfig_file="conf/gateway.properties" -jar connector-bridge-1.0-SNAPSHOT.war 2>&1 1>./logs/connector-bridge.log
