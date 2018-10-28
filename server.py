import socket

SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000

handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (SERVER_ADDRESS,SERVER_PORT)
print("server {} is listening {}".format(SERVER_ADDRESS,SERVER_PORT))
print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")
handler.bind(address)
file = open('soldier.jpeg','wb')
handler.listen(1)


while True:
    print("waiting for connection")
    con, client_address = handler.accept()
    line = con.recv(1024)
    while line:
        print("Reciving file...")
        file.write(line)
        line = con.recv(1024)
    file.close()
    print("Done")
    con.close()
