import socket
import threading

UDP_IP = "127.0.0.1"   # IP serwera
UDP_PORT = 5005

joined = False

# tworzenie socketu UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# automatyczny lokalny port klienta
sock.bind(("", 0))

print("Klient uruchomiony")







while True:

    msg = input("wiadomosc: ").strip()

    if msg == "exit":
        
        break

    if not joined:
        if msg == "join":
            sock.sendto("JOIN".encode(), (UDP_IP, UDP_PORT))
            joined = True
            print("Wysłano prośbę dołączenia")
        else:
            print("Wpisz join żeby dołączyć")
        continue

    sock.sendto(msg.encode(),(UDP_IP, UDP_PORT))







# funkcja odbierająca wiadomości
def receive():

    while True:

        data, addr = sock.recvfrom(1024)

        message = data.decode()

        print(f"\nNowa wiadomość: {message} z adresu {addr}")

# stworzenie wątku odbierającego
thread = threading.Thread(target=receive)

# wątek zamknie się razem z programem
thread.daemon = True

# start wątku
thread.start()