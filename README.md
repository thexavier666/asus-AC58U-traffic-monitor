# Router Traffic Plotter

I wanted to plot the a 24 hour network usage of my ASUS router and there was no built in facilty by the firmware.
So I decided to create my own logger.
It's written in shell, so it should work in any POSIX-compliant router.

## Installing the logger

There are two files in this repository

1. `monitor.sh`
2. `convert.py`

Place the `monitor.sh` in your router.
Ideally, you should place it in such a partition which has enough space.
Accordingly you should change the `dump_archive` directory present in the file.
Also, change the interface list as per your router's configuration.

Start the process using `nohup` or `screen`.

	nohup monitor.sh

If your router does not support those applications, you need to have another device which can login to the router and run the script.
Unfortunately, your secondary device needs to be on.

My ASUS router does not have `ssh-keygen`, so I could not automate the dumping of log files.
You can tell your secondary device to pull the log file right after the router dumps the log.

## Plotting the data

You need to have `matplotlib` package.
Replace the logfile name in `convert.py` in the `filename` variable.

## To-do

* Seperate config file
* Automate dumping of log files
