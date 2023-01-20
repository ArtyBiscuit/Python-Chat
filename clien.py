import socket
pseudo = "default"

host = input("IP:")
port = int(input("Port:"))
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
        msg = msg.encode("utf8")
        socket.sendall(msg)
        if msg == "/deco":
            break
    socket.close()