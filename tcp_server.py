import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
sock.bind((host, port))

print(f"server running at http://{host}:{port}")
try:
    while True:
        sock.listen()
except KeyboardInterrupt:
    print("cleaning up")
    sock.close()
