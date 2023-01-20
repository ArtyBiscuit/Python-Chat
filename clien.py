import socket
import threading




pseudo = "default"
host = input("IP:")
port = int(input("Port:"))
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pseudo = input("Enter Your Name: ")
class   update_listener(threading.Thread):
            def __init__(self, socket):
                threading.Thread.__init__(self)
                self.socket = socket
            def run(self):
                print("yep gro!")
                while True:
                        data = self.socket.recv(1024)
                        data = data.decode("utf8")
                        if data:
                                print(data)

try:
    socket.connect((host, port))
    print("cennecte !")
    data = pseudo
    data = data.encode("utf8")
    socket.sendall(data)
except ConnectionError:
    print("connection Error.")
    socket.close()
finally:
    test = update_listener(socket)
    test.start()
    while True:
        msg = input("MSG: ")
        msg = msg.encode("utf8")
        socket.sendall(msg)
        if msg == "/deco":
            break
    socket.close()