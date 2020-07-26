# upper and lower limit of the graph
lim_val	= [0,110]

# size of a byte
TO_BITS	= 8

# size of a kilobyte in byte
TO_KB	= 1024

# size of a megabyte in byte
TO_MB	= 1024*1024

# interfaces to plot
plt_id  = ["eth0", "eth1", "wifi1"]

# list of possible interfaces
data_legend = {
	"wifi0":{"RX_pos":1, "TX_pos":2, "type":"2.4 GHz Wifi"},
	"wifi1":{"RX_pos":3, "TX_pos":4, "type":"(Work Laptop) Wifi"},
	"ath0" :{"RX_pos":5, "TX_pos":6, "type":"2.4 GHz Wifi"},
	"ath1" :{"RX_pos":7, "TX_pos":8, "type":""},
	"eth0" :{"RX_pos":9, "TX_pos":10,"type":"Internet"},
	"eth1" :{"RX_pos":11,"TX_pos":12,"type":"(Personal Servers) LAN"},
	"br0"  :{"RX_pos":13,"TX_pos":14,"type":"Internet"}
}
