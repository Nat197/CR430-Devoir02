from inputimeout import inputimeout, TimeoutOccurred
import socket
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
   
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")
    string = ""
    try:
        string = inputimeout(prompt="Entrer votre commande:", timeout=20)
    except TimeoutOccurred:
        print("Délai dépassé")
    if(string):
        server.send(bytes(string, "utf-8"))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")
    
        