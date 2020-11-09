#Package importation
import socket
import sys
from datetime import datetime

#Test the number of received parameters in argv
if len(sys.argv) < 2:
   print('There\'s no parameter.')
   exit()
elif len(sys.argv) > 2:
   print('To much parameter.')
   exit()

IP = sys.argv[1] #assign the ip parameter entered
t1 = datetime.now() #catch the time the execution begin
ttl = 0.025 #time to leave
PORT = 6332 #port number
socket.setdefaulttimeout(ttl) #set the default time of the socket

#Establish a connection on the IP and the Port and test the connectivity
def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,PORT))
   if result == 0:
      return 1
   else :
      return 0

#Ping method
def ping(addr):
      if (scan(addr)):
         t2 = datetime.now()
         total = t2 - t1
         print('Succes !!')
         print ("from {}: ttl={} time={} ms".format(addr,ttl,total))
      else:
          print('Port unreachable')

#Ping the IP
ping(IP)
