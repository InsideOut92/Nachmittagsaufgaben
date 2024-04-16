import ipaddress

def calculate_ipv6(self):
    ip = self.ipv6_entry.get()
    cidr = int(self.cidr_value.get())
    if self.validate_ipv6(ip):
        network = ipaddress.IPv6Network(ip + '/' + str(cidr), strict=False)
        self.ipv6_subnet_value.config(text=str(network.netmask))
        self.ipv6_network_value.config(text=str(network.network_address))
        self.ipv6_host_min_value.config(text=str(network.network_address + 1))
        self.ipv6_host_max_value.config(text=str(network.broadcast_address - 1))
    else:
        self.show_error_message("Ungültige IPv6-Adresse! Bitte korrigieren Sie die Eingabe.")

def validate_ipv6(self, ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
