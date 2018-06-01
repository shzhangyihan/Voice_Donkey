import socket
import sys

HOST = 'ZhangYihandeMBP.attlocal.net'    # The remote host
PORT = 8888                     # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    w = raw_input()
    s.send(w)
s.close()
