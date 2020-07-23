#!/usr/bin/python3

import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import datetime
from matplotlib.dates import DateFormatter

filename = sys.argv[1] 

time_dur = 5

TO_BITS=8
TO_KB=1024
TO_MB=1024*1024

data_legend = {
	"wifi0":{"RX_pos":1, "TX_pos":2, "type":"2.4 GHz Wifi"},
	"wifi1":{"RX_pos":3, "TX_pos":4, "type":"(Work Laptop) Wifi"},
	"ath0" :{"RX_pos":5, "TX_pos":6, "type":"2.4 GHz Wifi"},
	"ath1" :{"RX_pos":7, "TX_pos":8, "type":""},
	"eth0" :{"RX_pos":9, "TX_pos":10,"type":"Internet"},
	"eth1" :{"RX_pos":11,"TX_pos":12,"type":"(Personal Servers) LAN"},
	"br0"  :{"RX_pos":13,"TX_pos":14,"type":"Internet"}
}

def cal_rate(curr,prev,period):

	tmp_curr = curr[1:]
	tmp_prev = prev[1:]

	tmp_val = []

	for i in range(len(tmp_curr)):

		bw_rate = (float(tmp_curr[i]) - float(tmp_prev[i]))/float(period)

		bw_rate = (bw_rate * TO_BITS) / (TO_MB)

		tmp_val.append(bw_rate)

	return tmp_val

def plot_this(rate_series, time_series):
	np_rate_series = np.asarray(rate_series, dtype=np.float32)

	up_lim = np_rate_series.size

	np_xaxis = time_series

	plt_id  = ["eth0", "eth1", "wifi1"]
	lim_val = [0,110]
	int_num = len(plt_id) 
	date_format = "%H:%M"

	for i in range(int_num):
	
		plt.subplot(int(str(int_num) + "2" + str(2*i+1)))
		plt.ylim(lim_val)
		plt.plot_date(np_xaxis, np_rate_series[:,data_legend[plt_id[i]]["RX_pos"]], linestyle='solid', marker='None')
		plt.ylabel("Bandwidth (Mbps)")
		plt.title(data_legend[plt_id[i]]["type"] + " Download")
		plt.grid(True)

		xaxis_tick_format = DateFormatter(date_format)
		plt.gca().xaxis.set_major_formatter(xaxis_tick_format)
	
		plt.subplot(int("32" + str(2*i+2)))
		plt.ylim(lim_val)
		plt.plot_date(np_xaxis, np_rate_series[:,data_legend[plt_id[i]]["TX_pos"]], linestyle='solid', marker='None')
		plt.ylabel("Bandwidth (Mbps)")
		plt.title(data_legend[plt_id[i]]["type"] + " Upload")
		plt.grid(True)

		xaxis_tick_format = DateFormatter(date_format)
		plt.gca().xaxis.set_major_formatter(xaxis_tick_format)

	plt.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.05, wspace=0.15, hspace=0.28)

	plt.show()
	

def main():
	fp = csv.reader(open(filename,'r'))

	row_prev = next(fp)

	rate_series = []
	time_series = []

	for row in fp:
		time_dur = int(row[0]) - int(row_prev[0])
		time_series.append(datetime.datetime.fromtimestamp(float(row[0])))

		curr_rate = cal_rate(row, row_prev, time_dur)
		curr_rate.insert(0,time_dur)
		rate_series.append(curr_rate)

		row_prev = row

	plot_this(rate_series, time_series)

if __name__ == '__main__':
	main()
