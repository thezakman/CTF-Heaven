Who's that pokemon??

It's `masscan`!

masscan is a tool for scanning services, like nmap. In contrast to nmap, masscan uses SYN COOKIE packets or something to make this process a LOT faster!

To get started try a simple scan of the entire internet for ssh servers.

`masscan --port 22 --range 0.0.0.0/0 --exclude 255.255.255.255 --rate 1000000`

this will instantly start returning massive amounts of open ports!

Lets just go ahead and hit every port on the internet!

`masscan --ports 0-65535 --range 0.0.0.0/0 --exclude 255.255.255.255 --rate 1000000`

How about all open ports in syria?

`masscan --ports 0-65535 --exclude 255.255.255.255 --rate 1000000 --range 5.0.0.0/16 5.104.128.0/21 5.134.200.0/21 5.134.224.0/19 31.9.0.0/16 31.193.64.0/20 37.48.128.0/18 37.48.192.0/19 46.53.0.0/17 46.57.128.0/17 46.58.128.0/17 46.161.192.0/18 46.213.0.0/16 77.44.128.0/17 78.110.96.0/20 78.155.64.0/19 82.137.192.0/18 88.86.0.0/19 90.153.128.0/17 91.144.0.0/18 94.141.192.0/19 94.252.128.0/17 95.87.112.0/21 95.140.96.0/20 95.159.0.0/18 109.238.144.0/20 130.0.240.0/20 130.180.128.0/18 178.52.0.0/16 178.171.128.0/17 178.253.64.0/18 185.4.84.0/22 185.19.124.0/22 185.23.184.0/22 185.24.60.0/22 185.41.84.0/22 185.52.232.0/22 185.54.132.0/22 185.84.48.0/22 185.84.236.0/22 185.92.28.0/22 185.92.88.0/22 185.96.108.0/22 185.110.104.0/22 185.114.240.0/22 185.121.184.0/22 188.139.128.0/17 188.160.0.0/16 188.229.128.0/17 188.247.0.0/19 212.11.192.0/19 213.178.224.0/19 217.20.208.0/20 195.60.236.0/22 196.2.4.0/22 198.51.143.0/24 198.51.144.0/23 198.51.146.0/24`

masscan supports grabbing banners with --banners, the --rate argument makes things go fast but can sometimes result in dropped responses. 

If you have multiple shells to scan from, you can use --shard 1/2 and --shard 2/2 and they will scan your targets without overlapping. you can set any amount of shards.

you can also clean up output with --open-only

Thats about it, this is a simple tool built for fast scanning. If you find a target, try running a masscan against all it's ports. This might take nmap hours and masscan minutes or seconds. Feed your results into nmap for application service detection.

Enjoy!
- kernel zero day
