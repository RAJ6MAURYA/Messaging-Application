import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
client.connect((SERVER, PORT))
DISCONNECT = "!DISCONNECT"
connected = True


def listen():
    global connected
    while(connected):
        msg = client.recv(1024).decode()
        print(f'{msg}')


def send(msg):
    client.send(msg.encode())
    if(msg == DISCONNECT):
        client.close()


def init():
    thread1 = threading.Thread(target=listen, args=[])
    thread1.start()
