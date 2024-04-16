import ipaddress

def calculate_ipv4(self):
    ip = self.ipv4_entry.get()
    cidr = int(self.cidr_value.get())
    if self.validate_ipv4(ip):
        network = ipaddress.IPv4Network(ip + '/' + str(cidr), strict=False)
        self.ipv4_subnet_value.config(text=str(network.netmask))
        self.ipv4_network_value.config(text=str(network.network_address))
        self.ipv4_broadcast_value.config(text=str(network.broadcast_address))
        self.ipv4_host_min_value.config(text=str(network.network_address + 1))
        self.ipv4_host_max_value.config(text=str(network.broadcast_address - 1))
    else:
        self.show_error_message("Ungültige IPv4-Adresse! Bitte korrigieren Sie die Eingabe.")

def validate_ipv4(self, ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
