import socket

HOST = '127.0.0.1'  # Localhost
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, port))
print('Started listening')
s.listen()
client_socket, addr = s.accept()
print(addr)
data = client_socket.recv(1024)

client_socket.close()
print(data)
