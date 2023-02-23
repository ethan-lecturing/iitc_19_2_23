import socket

server_ip = '127.0.0.1'  # Localhost
server_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
print()
s.send(b'Hello world')
s.close()
