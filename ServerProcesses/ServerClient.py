import socket

HOST, PORT = '127.0.0.1', 5734

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ECHO 1024")
    data = s.recv(1024)

print(f"Received {data!r}")