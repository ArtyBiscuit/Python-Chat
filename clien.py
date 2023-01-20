import socket
pseudo = "default"

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pseudo = input("Enter Your Name: ")

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
    while True:
        msg = input("MSG: ")
        if msg == "/deco":
            break
        msg = msg.encode("utf8")
        socket.sendall(msg)
    socket.close()