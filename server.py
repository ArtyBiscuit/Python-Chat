import socket
import threading


class ThreadClient(threading.Thread):
        def __init__(self, conn):
                threading.Thread.__init__(self)
                self.conn = conn
        def run(self):
                data = self.conn.recv(16)
                data = data.decode("utf8")
                name = data
                print("<", name, ">", "connected to the server from:", address)
                print(threading.current_thread())
                while True:
                        data = self.conn.recv(1024)
                        data = data.decode("utf8")
                        if data == "/deco":
                                print("<", name, ">", "disconnected from the server")
                                break
                        if data:
                                print("Neme:", name, "|", data)

host = ''
port = int(input("Port:"))
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Server open on port:", port)

while True:
        socket.listen(2)
        conn, address = socket.accept()
        #print("connection from:", address)
        my_thread = ThreadClient(conn)
        my_thread.start()
conn.close()
socket.close()

