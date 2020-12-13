import json
import socket

OPEN_PORTS = []
PORTS_DATA_FILE = "./common_ports.json"


def extract_json_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def get_ports_info():
    data = extract_json_data(PORTS_DATA_FILE)
    ports_info = {int(k): v for (k, v) in data.items()}
    return ports_info

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
    ports_info = get_ports_info()

    for port in ports_info.keys():
        try:
            print(f"Scanning: {ip_addr}:{port}")
            scan_port(ip_addr, port)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

    print("Open Ports:")
    for port in OPEN_PORTS:
        print(str(port), ports_info[port])
