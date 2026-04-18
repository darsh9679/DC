import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000)) # Use server's IP

def receive():
    while True: print(f"\n{client.recv(1024).decode()}")

threading.Thread(target=receive, daemon=True).start()

while True: client.send(input("You: ").encode())