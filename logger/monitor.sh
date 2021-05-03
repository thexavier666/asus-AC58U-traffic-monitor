#!/bin/sh

# loading all variables
. ./config

mkdir -p $DUMP_DIR$DUMP_ARCHIVE

DUMP_FILENAME="$(GET_LOGFILE_NAME)"

while [ True ]
do
	# list of interfaces which we want to monitor
    set -- "wifi0" "wifi1" "ath0" "ath1" "eth0" "eth1" "br0"

	# getting the current time
	curr_time=$(date +%R:%S)
	curr_time_utc=$(date +%s)
	
	str_dump="$curr_time_utc"
	
	# iterating through each interface
	while [ $# -gt 0 ]
	do
		# getting rx and tx stats
		rx_val=$(cat /sys/class/net/$1/statistics/rx_bytes)
		tx_val=$(cat /sys/class/net/$1/statistics/tx_bytes)
		output="$rx_val,$tx_val"

		str_dump="$str_dump,$output"
		shift
    done

	# putting stats in log file
	echo "$str_dump" >> $DUMP_DIR$DUMP_FILENAME

	curr_time=$(echo $curr_time | cut -d':' -f1,2)

	# time to roll over to new log file
	if test $curr_time = $REFRESH_TIME
	then
		mv $DUMP_DIR$DUMP_FILENAME $DUMP_DIR$DUMP_ARCHIVE

		DUMP_FILENAME="$(GET_LOGFILE_NAME)"

		sleep $SLEEP_LONG
	else
		sleep $SLEEP_SHORT
	fi
done
