# portscanner.py

import socket
HOST = "127.0.0.1"

for i in range(0, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((HOST, i))
    if(result==0):
        print("TCP:{} aberta".format(i))
