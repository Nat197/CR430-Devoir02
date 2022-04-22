from inputimeout import inputimeout, TimeoutOccurred
import socket
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    buffer = client.recv(1024)
    buffer = buffer.decode("utf-8")
    close = False
    print(f"client: {buffer}")
    string = ""
    try:
        string = inputimeout(prompt="Entrer votre commande:", timeout=20)
    except TimeoutOccurred:
        print("Délai dépassé")
    if(string):
        client.send(bytes(string, "utf-8"))
        if(string == "fichier"):
            filename = client.recv(1024).decode("utf-8")
            print(f"file name : {filename}")
            file = open(filename, "w")
            client.send(bytes("Filename received", "utf-8"))
            data = client.recv(1024).decode("utf-8")
            file.write(data)
            client.send(bytes("Filedata received", "utf-8"))
            file.close()
            client.close()
            close = True
            
    if(not close):
        buffer = client.recv(1024)
        buffer = buffer.decode("utf-8")
        print(f"Server: {buffer}")
    
        