# Router Traffic Plotter

I wanted to plot a 24 hour network throughput time-series of my ASUS router and there was no built in facilty provided by the firmware.
I also didn't want to flash a custom firmware for this feature.
So I decided to create my own logger.

### Prerequisites

1. Router must support a POSIX shell
2. Should be able to `ssh` into it
3. Should support `cut`, `awk` and `sed`

## Installing the logger

* Place `config` and `monitor.sh` in your router in the same directory.
Ideally, you should place it in such a partition which has enough space to store atleast 2 log file dumps.
* Change the `DUMP_ARCHIVE` directory present in `config`.
This dictates where the log files will be written.
* Change the interface list as per your router setup.
Check interface list using `ifconfig` or `ip a`.

## Starting the logger

Start the process using `nohup` or `screen`.

	nohup monitor.sh

**Note** - If your router does not support `nohup` or similar applications, you need to have another device which can login to the router and run the script.
Unfortunately, your secondary device needs to be on.

Since my ASUS router does not have `ssh-keygen`, I could not automate the dumping of log files.
You can also tell your secondary device to pull the log file right after the router dumps the log.
Installing something like OpenWrt alleviates the problem.

## Plotting the data

You need to have `matplotlib` Python package.
You can run this on your own machine, once the data has been collected.
To plot, run the command

	./plot.py <filename> -1 -1

## To-do

* ~~Seperate config file~~
* Automate dumping of log files
