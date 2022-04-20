import os
import nmap
from faker import Faker


class Server:

    def __init__(self):
        self.ports = [22, 21, 23, 3389, 3306, 80, 443, 25, 110, 135, 1433, 5632, 5900, 25565]
        self.host = None
        self.valid_ports = []
        self.valid_ips = []
        self.map = nmap.PortScanner()
        if not os.path.exists('invalid.txt'):
            open('invalid.txt', 'w').writelines('')
        if not os.path.exists('valid.txt'):
            open('valid.txt', 'w').writelines('')

    def next(self):
        while True:
            self.host = Faker().ipv4()
            if self.host not in open('invalid.txt', 'r').read() and self.host not in open('valid.txt', 'r').read():
                return self.host

    def save(self, option='valid'):
        with open(f'{option}.txt', 'a') as f:
            if option == 'valid':
                f.writelines(f'{self.host},{",".join(str(p) for p in self.valid_ports)}\n')
            else:
                f.writelines(f'{self.host},')
        f.close()

    def run(self, verbose=False):
        while True:
            self.next()
            try:
                self.map.scan(self.host, arguments=f'-p {",".join(str(port) for port in self.ports)} --open')
                for ports in self.ports:
                    result = self.map[self.host].has_tcp(ports)
                    if result:
                        self.valid_ips.append([self.host, ports])
                self.valid_ports = self.map[self.host]["tcp"].keys()
                print(f'Results {self.host}: {self.map[self.host]["tcp"].keys()}')
                self.save()
            except Exception as e:
                self.save('invalid')
                if verbose:
                    print(f'error: {e}')
