#!/usr/bin/python3

import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import datetime
from matplotlib.dates import DateFormatter

# importing all constants
import config

def cal_rate(curr,prev,period):

    tmp_curr = curr[1:]
    tmp_prev = prev[1:]

    tmp_val = []

    for i in range(len(tmp_curr)):

        bw_rate = (float(tmp_curr[i]) - float(tmp_prev[i]))/float(period)

        bw_rate = (bw_rate * config.TO_BITS) / (config.TO_MB)

        tmp_val.append(bw_rate)

    return tmp_val

def plot_this(rate_series, time_series):
    np_rate_series = np.asarray(rate_series, dtype=np.float32)

    up_lim = np_rate_series.size

    np_xaxis = time_series

    int_num = len(config.plt_id) 
    date_format = "%H:%M"

    for i in range(int_num):
        plt.subplot(int_num,2,2*i+1)
        plt.ylim(config.lim_val)
        plt.plot_date(np_xaxis, np_rate_series[:,config.data_legend[config.plt_id[i]]["RX_pos"]], linestyle='solid', marker='None')
        plt.ylabel("Bandwidth (Mbps)")
        plt.title(config.data_legend[config.plt_id[i]]["type"] + " Download")
        plt.grid(True)

        xaxis_tick_format = DateFormatter(date_format)
        plt.gca().xaxis.set_major_formatter(xaxis_tick_format)
    
        plt.subplot(int_num,2,2*i+2)
        plt.ylim(config.lim_val)
        plt.plot_date(np_xaxis, np_rate_series[:,config.data_legend[config.plt_id[i]]["TX_pos"]], linestyle='solid', marker='None')
        plt.ylabel("Bandwidth (Mbps)")
        plt.title(config.data_legend[config.plt_id[i]]["type"] + " Upload")
        plt.grid(True)

        xaxis_tick_format = DateFormatter(date_format)
        plt.gca().xaxis.set_major_formatter(xaxis_tick_format)

    plt.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.05, wspace=0.15, hspace=0.28)

    plt.show()
    

def main():
    if len(sys.argv) != 4:
        print("usage: {} <filename> <lower limit> <upper limit>\n".format(sys.argv[0]))
        print("       if you don't want to use limits, put -1 instead\n")
        print("       Example:")
        print("       ./convert file.csv -1 -1")

        return 0

    filename = sys.argv[1] 
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

    clip_lower = 0
    clip_upper = len(rate_series)+1


    if sys.argv[2] != "-1" and sys.argv[3] != "-1":
        clip_lower = int(sys.argv[2])
        clip_upper = int(sys.argv[3])+1

    plot_this(rate_series[clip_lower:clip_upper], time_series[clip_lower:clip_upper])

if __name__ == '__main__':
    main()
