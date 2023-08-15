import socket 
import random
import string

# socket instance
"""
af_inet : only accept ipv4
sock_stream : only tcp connection
"""
server_obj = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_add = '127.0.0.1'
port = 5555

server_obj.bind((ip_add, port))
server_obj.listen()

connection_obj, _ = server_obj.accept()

if connection_obj:
    print("Server connected to Client")
    connection_obj.send(b"type the messge")

    data_receive = connection_obj.recv(1024)

    while data_receive != b'stop':
        print("{}: {}".format("Client Message: ", data_receive.decode('utf-8')))

        server_input = random.choice(string.ascii_letters)
        connection_obj.send(server_input.encode('utf-8'))
        data_receive = connection_obj.recv(1024)
