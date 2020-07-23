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
	
	while [ $# -gt 0 ]
	do
		# get statistics for interface $1
		# get 1st column
		# get only 4th and 6th row
		# format them into csv string
		output=$(ip -s link ls $1 | awk '{print $1}' | sed -n -e 4p -e 6p | sed 'H;1h;$!d;x;y/\n/,/')

		str_dump="$str_dump,$output"
		shift
        done

	echo "$str_dump" >> $DUMP_DIR$DUMP_FILENAME

	curr_time=$(echo $curr_time | cut -d':' -f1,2)

	if test $curr_time = $REFRESH_TIME
	then
		mv $DUMP_DIR$DUMP_FILENAME $DUMP_DIR$DUMP_ARCHIVE

		DUMP_FILENAME="$(GET_LOGFILE_NAME)"

		sleep $SLEEP_LONG
	else
		sleep $SLEEP_SHORT
	fi
done
