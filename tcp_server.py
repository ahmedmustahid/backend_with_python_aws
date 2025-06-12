import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
sock.bind((host, port))

print(f"server running at http://{host}:{port}")
try:
    sock.listen(2)
    while True:
        conn, addr = sock.accept()
        print(f"connected to {addr}")
        ret_data = conn.recv(1024)
        if not ret_data:
            break
        ret_string = ret_data.decode()
        print(f"client says: {ret_string}")

        # Build a minimal HTTP response
        body = f"Echo: {ret_string}"
        response = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(body)}\r\n"  # Tell curl how much data to expect
            "Content-Type: text/plain\r\n"
            "\r\n"  # End of headers
            f"{body}"
        )
        conn.sendall(response.encode())
        conn.close()  # Close the connection (optional if Content-Length is set)
except KeyboardInterrupt:
    print("shutting down...")
finally:
    sock.close()
