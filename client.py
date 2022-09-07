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


def send(user_name):
    global connected
    while(connected):
        msg = input()
        msg= f'[{user_name}]'+msg
        client.send(msg.encode())
        if(msg == DISCONNECT):
            connected = False
    client.close()


def init():
    user_name = input("Enter your name: ")
    thread1 = threading.Thread(target=listen, args=[])
    thread2 = threading.Thread(target=send, args=[user_name])
    thread1.start()
    thread2.start()

init()