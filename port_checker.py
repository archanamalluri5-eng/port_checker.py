import socket

host = input("Enter Host (e.g., localhost): ")
port = int(input("Enter Port Number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

sock.close()
