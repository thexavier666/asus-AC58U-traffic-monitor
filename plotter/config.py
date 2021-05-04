# upper and lower limit of the graph
lim_val	= [0,110]

# size of a byte
TO_BITS	= 8

# size of a kilobyte in byte
TO_KB	= 1024

# size of a megabyte in byte
TO_MB	= 1024*1024

# interfaces to plot
plt_id  = ["wlan0", "wlan1", "eth0", "eth1", "br-lan"]

# list of interfaces, column position in data file, and a short description
data_legend = {
	"wlan0" :{"RX_pos":1, "TX_pos":2, "type":"2.4 GHz Wifi"},
	"wlan1" :{"RX_pos":3, "TX_pos":4, "type":"5.0 Ghz Wifi"},
	"eth0"  :{"RX_pos":5, "TX_pos":6, "type":"LAN Traffic"},
	"eth1"  :{"RX_pos":7, "TX_pos":8, "type":"WAN Traffic"},
	"br-lan":{"RX_pos":9, "TX_pos":10,"type":"Don't know"}
}
