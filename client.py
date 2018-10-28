import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (SERVER_ADDRESS,SERVER_PORT)

# Connect to server
sock.connect(address)

# OPEN FILE

file = open('/Users/kobiKanetti/Desktop/Project/projectFolder/soldier.jpeg','rb')
line = file.read(1024)

# READ FILE (1024 BYTE EACH READ) WITH WHILE TILL END
while line:
    print("Sending file...")
    sock.send(line)
    line = file.read(1024)
file.close()
print("Done sending")

# AT END OF FILE, CLOSE SOCKET
sock.shutdown(socket.SHUT_WR)
print(sock.recv(1024))
sock.close()
