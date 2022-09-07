# server side
import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVER, PORT))

totalClients = []


def handle_client(conn):
    connected = True
    while connected:
        msg = conn.recv(1024).decode()
        if msg:
            if(msg == DISCONNECT):
                connected = False
            print(f"{msg}")
            broadcast(conn, msg)
    totalClients.remove(conn)
    conn.close()


def broadcast(conn, msg):
    for clients in totalClients:
        if(conn != clients):
            send_message(clients, msg)


def send_message(conn, msg):
    conn.send(msg.encode())


def send():
    while(True):
        msg = input()
        msg = "[SERVER] "+msg
        broadcast(None, msg)


"""def init(conn):
    conn.send(("Enter your name:").encode())
    name = conn.recv(100).decode()
    return name"""


def master():
    print("Server is Listening...!\n")
    while(True):
        server.listen()
        conn, addr = server.accept()
        #client_name = init(conn)
        totalClients.append(conn)
        thread = threading.Thread(
            target=handle_client, args=(conn,))
        thread.start()
        print(f"TOTAL Connected: {threading.active_count()-3}")


main_thread = threading.Thread(target=master, args=[])
main_thread.start()
send = threading.Thread(target=send, args=[])
send.start()
