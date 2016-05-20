import socket
import sys
import toapp
import time

# Create a TCP/IP socket

# Bind the socket to the port
server_address = ('0.0.0.0',5007)
print >>sys.stderr, 'starting up on %s port %s' % server_address


# Listen for incoming connections

data_sent=''
while True:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     sock.bind(server_address)
     sock.listen(1)
     print >>sys.stderr, 'waiting for a connection'
     connection, client_address = sock.accept() 
     try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
             time.sleep(2)             
             data = connection.recv(1500)
             data_to_process=data.rstrip()
             print >>sys.stderr, 'received "%s"' % data
             if data:
                data_sent=toapp.process(data_to_process)
                data_sent=data_sent+'\n'
                print(data_sent)
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data_sent)
                break
             else:
                print >>sys.stderr, 'no more data from', client_address
                break                      
     finally:          
        # Clean up the connection
        print 'closing connection'
        connection.close() 
     
 
   

