import socket

UDP_IP = ""
UDP_PORT = 5005 #port na komputerze na który klient wysyła dane 

#tworzenie kanału komunikacji sieciowej
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET obsługa adresów IPv4|| SOCK_DGRAM używamy UDP
#przypinanie kanału do podanych adresów
sock.bind((UDP_IP, UDP_PORT))

clients = []

print("serwer działa")

while True:
    #recvfrom - czeka na pakiet UDP i odbiera go zwracając tupla(dane w bajtach, adres nadawcy), kod czeka puki pakiet nie nadejdzie 
    data, addr = sock.recvfrom(1024) #addr to kolejny tuple (adres ip, port)

    message = data.decode()

    if addr not in clients:
        clients.append(addr)
        print("Nowy klient:", addr)

    print(f"Odebrano od {addr}: {message}")

    for client in clients:
        if client != addr:
            sock.sendto(
                f"{addr}: {message}".encode(),
                client)



