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
                #print(name,"connected to the server")
                while True:
                        data = self.conn.recv(1024)
                        data = data.decode("utf8")
                        if data:
                                print(name,":", data)

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Server open.")

N = 0

while True:
        socket.listen(2)
        conn, address = socket.accept()
        print("Clien connecter...")
        my_thread = ThreadClient(conn)
        my_thread.start()
        if N == 1:
                break
conn.close()
socket.close()
