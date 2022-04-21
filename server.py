import socket


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Established - {address[0]}:{address[1]}")

        commande = client.recv(1024)
        commande = commande.decode("utf-8")
        commande = commande.upper()

        if commande == "TIME":
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            message = current_time


        elif commande == "IP":
            ipclient = address[0]
            message = "Votre adresse IP est : {ipclient}"

        elif commande == "EXIT":
            message = "Fermeture de la connexion..."
            client.close()
        
        else :
            message = "Cette commande n'est pas valide ou prise en charge par le serveur"

        client.send(bytes(message, "utf-8"))

        
