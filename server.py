from ensurepip import version
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
        client.send(bytes(f"Connection Established - {address[0]}", "utf-8"))
        client.settimeout(5)
        try:
            commande = client.recv(1024)
            commande = commande.decode("utf-8")
            commande = commande.upper()
            print(commande)

            if(not commande):
                client.send(b"Timeout")
                client.close()
            
            elif commande == "TIME":
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                message = current_time
        
            elif commande == "OS":
                import platform
                system = platform.system()
                release = platform.release()
                version = platform.version()

                message = f"Systeme d'exploitation : {system}\n Release : {release}\n Version : {version}"
                client.send(bytes(message, "utf-8"))

            elif commande == "IP":
                ipclient = address[0]
                message = f"Votre adresse IP est : {ipclient}"
                client.send(bytes(message, "utf-8"))

            elif commande == "FICHIER":
                file = open("", "r")
                data = file.read(1024)
                client.send(bytes("", "utf-8"))
                print("ok")

            elif commande == "EXIT":
                client.send(bytes("Fermeture de la connexion...", "utf-8"))
                client.close()

            else:
                message = f"Cette commande n'est pas valide ou prise en charge par le serveur"
                client.send(bytes(message, "utf-8"))

        except socket.timeout:
            client.send(bytes("Le délai a été dépassé la connexion a été terminée...", "utf-8"))
            print("TIMEOUT du client")
            break

        
