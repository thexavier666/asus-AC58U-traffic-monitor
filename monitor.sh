#!/bin/sh

# time at which log is to be dumped
refresh_time="07:00"

sleep_long="60"
sleep_short="5"

dump_dir="/jffs/net_monitor/"
dump_archive="stats"

# log file name
dump_filename="netlog-$(date +%F).csv"

mkdir -p $dump_dir$dump_archive

while [ True ]
do
	# list of interfaces which we want to monitor
        set -- "wifi0" "wifi1" "ath0" "ath1" "eth0" "eth1" "br0"

	# getting the current time
	curr_time=$(date +%R:%S)
	curr_time_utc=$(date +%s)
	
	byte_count="$curr_time_utc"
	
	while [ $# -gt 0 ]
	do
		# get statistics for interface $1
		# get 1st column
		# get only 4th and 6th row
		# format them into csv string
		output=$(ip -s link ls $1 | awk '{print $1}' | sed -n -e 4p -e 6p | sed 'H;1h;$!d;x;y/\n/,/')

		byte_count="$byte_count,$output"
		shift
        done
       
	echo "$byte_count" >> $dump_dir$dump_filename

	curr_time=$(echo $curr_time | cut -d':' -f1,2)

	if test $curr_time = $refresh_time
	then
		mv $dump_dir$dump_filename $dump_dir$dump_archive

		dump_filename="netlog-$(date +%F).csv"

		sleep $sleep_long
	else
		sleep $sleep_short
	fi
done
