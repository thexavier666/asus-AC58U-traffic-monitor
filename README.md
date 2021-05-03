# Router Traffic Plotter

I wanted to plot a 24 hour network throughput time-series of my ASUS router and there was no built in facilty provided by the firmware.
Real-time plots provided by other firmwares tend to be slow or very resource-intensive.
I also didn't want to flash a custom firmware for this feature.
So I decided to create my own logger.

### Prerequisites

1. Router must support a POSIX shell
2. Should be able to `ssh` into it
3. Should support `cut`

## Installing the logger

Place `config` and `monitor.sh` in your router in the same directory.
Ideally, you should place it in such a partition which has enough space to store atleast 2 log file dumps.
Accordingly you should change the `DUMP_ARCHIVE` directory present in `config`.
Also, change the interface list as per your router's configuration.

Start the process using `nohup` or equivalent (`screen`, `tmux`).

	nohup monitor.sh

If your router does not support those applications, you need to have another device which can login to the router and run the script.
Unfortunately, your secondary device needs to be on.

Since my ASUS router does not have `ssh-keygen`, I could not automate the dumping of log files.
You can also tell your secondary device to pull the log file right after the router dumps the log.

## Plotting the data

You need to have `matplotlib` package.
You can plot on a different machine, once the data has been collected.
To plot, run the command

	./plot.py <filename> -1 -1

`<filename>` is the file containing the collected data.
The arguments `-1 -1` indicates plot the whole file, and not use any upper and lower time frame.
Check `plot.py` file for more details.

## Branch `openwrt`

I have recently installed the openwrt firmware on my ASUS router.
The changes are mentioned in the `openwrt` branch.
The main changes are

* using stats from `/sys/class/net` instead of `ip` since openwrt uses `ip` from the busybox utilities and it does not have the `s` flag (statistics flag)
* different set of interfaces
* different location of dumping log files

## To-do

* ~~Seperate config file~~
* Automate dumping of log files
