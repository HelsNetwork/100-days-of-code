import socket
import sys 

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 80)
tcp_socket.bind(address)

#listen on port 80
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()

    try:
        print("Connected to client IP: {}".format(client))
        
        while True:
            data = connection.recv(32)
            print("Received data: {}".format(data))

            if not data:
                break
    finally: 
        connection.close()
