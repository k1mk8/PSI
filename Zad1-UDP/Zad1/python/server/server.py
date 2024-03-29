import socket
import sys

if len(sys.argv) < 3:
   print("No server adrress or port was given")
   print("Setting default values: a: 172.18.0.2, p: 8000")
   localIP = '172.18.0.2'
   localPort = 8000
else:
   localIP = sys.argv[1]
   localPort = int(sys.argv[2])
bufferSize = 1024

UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while(True):
   # receiving name from client
   msg, addr1 = UDPServerSocket.recvfrom(bufferSize) 

   msg = msg.decode() 
      
   print(msg, addr1)