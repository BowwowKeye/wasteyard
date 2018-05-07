# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:54:21 2018

@author: 37580
"""
# Tcp Chat server
 
import socket, select
 
#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    print(CONNECTION_LIST)
    #Do not send the message to master socket and the client who has send us the message
    for connect in CONNECTION_LIST:
        if connect != server_socket and connect != sock :
            try :
                connect.send(bytes(message,'utf-8'))
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                CONNECTION_LIST.remove(connect)
                broadcast_data(connect,"\rClient (%s, %s) is offline" % ADDR_DICT[str(connect)])
                del ADDR_DICT[str(connect)]
                connect.close()


 
if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    ADDR_DICT={}
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print("Chat server started on port " + str(PORT))
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                ADDR_DICT[str(sockfd)]=addr
                print("\rClient (%s, %s) connected" % addr)
                 
                broadcast_data(sockfd, "\r[%s:%s] entered room\n" % addr)
             
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        mes="\r" + '<' + str(sock.getpeername()) + '> ' + data.decode(encoding='utf-8')
                        print(mes)
                        broadcast_data(sock, mes)                
                 
                except Exception as err:
                    print(err)
                    broadcast_data(sock, "Client (%s, %s) is offline" % ADDR_DICT[str(sock)])
                    print("Client (%s, %s) is offline" % ADDR_DICT[str(sock)])
                    CONNECTION_LIST.remove(sock)
                    sock.close()
                    continue
     
    server_socket.close()