import socket

from utils import extract_json_data


class PScan:

    PORTS_DATA_FILE = "./common_ports.json"

    def __init__(self):
        self.open_ports = []
        self.ports_info = {}
        self.remote_host = ""

    def get_ports_info(self):
        data = extract_json_data(PScan.PORTS_DATA_FILE)
        self.ports_info = {int(k): v for (k, v) in data.items()}

    @staticmethod
    def get_host_ip_addr(target):
        try:
            ip_addr = socket.gethostbyname(target)
        except socket.gaierror as e:
            print(f"C'è stato un errore... {e}")
        else:
            return ip_addr

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        conn_status = sock.connect_ex((self.remote_host, port))
        if conn_status == 0:
            self.open_ports.append(port)
        sock.close()

    def run(self):
        print("Programma scritto per solo scopo educativo!!!")
        target = input("Inserire Target: ")
        self.remote_host = self.get_host_ip_addr(target)
        self.get_ports_info()

        for port in self.ports_info.keys():
            try:
                print(f"Scanning: {self.remote_host}:{port}")
                self.scan_port(port)
            except KeyboardInterrupt:
                print("\nExiting...")
                break

        print("Open Ports:")
        for port in self.open_ports:
            print(str(port), self.ports_info[port])


if __name__ == "__main__":
    pscan = PScan()
    pscan.run()
    