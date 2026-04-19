import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen()
clients = []

def handle(c):
    while True:
        try:
            msg = c.recv(1024)
            [other.send(msg) for other in clients if other != c]
        except:
            clients.remove(c); break

while True:
    conn, _ = server.accept()
    clients.append(conn)
    threading.Thread(target=handle, args=(conn,)).start()