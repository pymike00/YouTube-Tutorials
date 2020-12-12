import socket

OPEN_PORTS = []


def get_host_ip_addr(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e:
        print(f"C'è stato un errore... {e}")
    else:
        return ip_addr

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip, port))
    if conn_status == 0:
        OPEN_PORTS.append(port)
    sock.close()


if __name__ == "__main__":
    print("Programma scritto per solo scopo educativo!!!")
    target = input("Inserire Target: ")
    ip_addr = get_host_ip_addr(target)
    while True:
        try:
            port = int(input("Inserire Porta: "))
            scan_port(ip_addr, port)
            print(OPEN_PORTS)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
