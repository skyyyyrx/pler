import socket
try:
    host = "webminer.pages.dev"
    port = 443
    sock = socket.create_connection((host, port), timeout=10)
    print("Connection OK")
except Exception as e:
    print(f"Connection failed: {e}")
