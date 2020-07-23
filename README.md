# Router Traffic Plotter

I wanted to plot a 24 hour network throughput time-series of my ASUS router and there was no built in facilty provided by the firmware.
I also didn't want to flash a custom firmware for this feature.
So I decided to create my own logger.

### Prerequisites

1. Router must support a POSIX shell
2. Should be able to `ssh` into it
3. Should support `awk` and `sed`

## Installing the logger

Place the `monitor.sh` in your router.
Ideally, you should place it in such a partition which has enough space to store atleast 2 log file dumps.
Accordingly you should change the `dump_archive` directory present in the file `monitor.sh`.
Also, change the interface list as per your router's configuration.

Start the process using `nohup` or `screen`.

	nohup monitor.sh

If your router does not support those applications, you need to have another device which can login to the router and run the script.
Unfortunately, your secondary device needs to be on.

Since my ASUS router does not have `ssh-keygen`, I could not automate the dumping of log files.
You can also tell your secondary device to pull the log file right after the router dumps the log.

## Plotting the data

You need to have `matplotlib` package.
You can this on your own machine, once the data has been collected.
Replace the logfile name in `convert.py` in the `filename` variable.

## To-do

* Seperate config file
* Automate dumping of log files
