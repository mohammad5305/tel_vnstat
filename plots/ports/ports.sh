#!/bin/bash
set -euo pipefail

PORTS=(8080 80)
LOG_FILE=ports.log
DATE=$(date +%H:%M)
CONNECTIONS=()

set -x 
for PORT in "${PORTS[@]}"
do
	#debug=$(netstat -atun | grep $PORT | awk '$6 == "ESTABLISHED" {print $5}' | awk -F: '{print $1}' | sort | uniq | wc -l)
	CONNECTIONS+=($(netstat -atun | grep $PORT | awk '$6 == "ESTABLISHED" {print $5}' | awk -F: '{print $1}' | sort | uniq | wc -l))
done
echo $DATE ${CONNECTIONS[@]} | tr -d '(' | tr -d ')' >> $LOG_FILE
