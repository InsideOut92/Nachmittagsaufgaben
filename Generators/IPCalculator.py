import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress

class IPAddressCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IP-Address Rechner by ChaosCoder")
        self.geometry("380x450")

        # IPv4 Widgets
        self.ipv4_label = ttk.Label(self, text="IPv4 Addresse:")
        self.ipv4_entry = ttk.Entry(self)
        self.ipv4_subnet_label = ttk.Label(self, text="Subnetz Maske:")
        self.ipv4_subnet_value = ttk.Label(self, text="")
        self.ipv4_network_label = ttk.Label(self, text="Netzwerk Addresse:")
        self.ipv4_network_value = ttk.Label(self, text="")
        self.ipv4_broadcast_label = ttk.Label(self, text="Broadcast Addresse:")
        self.ipv4_broadcast_value = ttk.Label(self, text="")
        self.ipv4_host_min_label = ttk.Label(self, text="Host Min:")
        self.ipv4_host_min_value = ttk.Label(self, text="")
        self.ipv4_host_max_label = ttk.Label(self, text="Host Max:")
        self.ipv4_host_max_value = ttk.Label(self, text="")

        # IPv6 Widgets
        self.ipv6_label = ttk.Label(self, text="IPv6 Addresse:")
        self.ipv6_entry = ttk.Entry(self)
        self.ipv6_subnet_label = ttk.Label(self, text="Subnetz Maske:")
        self.ipv6_subnet_value = ttk.Label(self, text="")
        self.ipv6_network_label = ttk.Label(self, text="Netzwerk Addresse:")
        self.ipv6_network_value = ttk.Label(self, text="")
        self.ipv6_host_min_label = ttk.Label(self, text="Host Min:")
        self.ipv6_host_min_value = ttk.Label(self, text="")
        self.ipv6_host_max_label = ttk.Label(self, text="Host Max:")
        self.ipv6_host_max_value = ttk.Label(self, text="")

        # CIDR Dropdown
        self.cidr_label = ttk.Label(self, text="CIDR:")
        self.cidr_value = tk.StringVar()
        self.cidr_dropdown = ttk.Combobox(self, textvariable=self.cidr_value)
        self.cidr_dropdown['values'] = tuple(range(1, 33))
        self.cidr_dropdown.current(0)

        # Buttons
        self.ipv4_button = ttk.Button(self, text="IPv4 Berechnen", command=self.calculate_ipv4)
        self.ipv6_button = ttk.Button(self, text="IPv6 Berechnen", command=self.calculate_ipv6)

        # Grid Layout
        self.ipv4_label.grid(row=0, column=0, sticky="e")
        self.ipv4_entry.grid(row=0, column=1, padx=5, pady=5)
        self.ipv4_subnet_label.grid(row=1, column=0, sticky="e")
        self.ipv4_subnet_value.grid(row=1, column=1, padx=5, pady=5)
        self.ipv4_network_label.grid(row=2, column=0, sticky="e")
        self.ipv4_network_value.grid(row=2, column=1, padx=5, pady=5)
        self.ipv4_broadcast_label.grid(row=3, column=0, sticky="e")
        self.ipv4_broadcast_value.grid(row=3, column=1, padx=5, pady=5)
        self.ipv4_host_min_label.grid(row=4, column=0, sticky="e")
        self.ipv4_host_min_value.grid(row=4, column=1, padx=5, pady=5)
        self.ipv4_host_max_label.grid(row=5, column=0, sticky="e")
        self.ipv4_host_max_value.grid(row=5, column=1, padx=5, pady=5)

        self.ipv6_label.grid(row=6, column=0, sticky="e")
        self.ipv6_entry.grid(row=6, column=1, padx=5, pady=5)
        self.ipv6_subnet_label.grid(row=7, column=0, sticky="e")
        self.ipv6_subnet_value.grid(row=7, column=1, padx=5, pady=5)
        self.ipv6_network_label.grid(row=8, column=0, sticky="e")
        self.ipv6_network_value.grid(row=8, column=1, padx=5, pady=5)
        self.ipv6_host_min_label.grid(row=9, column=0, sticky="e")
        self.ipv6_host_min_value.grid(row=9, column=1, padx=5, pady=5)
        self.ipv6_host_max_label.grid(row=10, column=0, sticky="e")
        self.ipv6_host_max_value.grid(row=10, column=1, padx=5, pady=5)

        self.cidr_label.grid(row=11, column=0, sticky="e")
        self.cidr_dropdown.grid(row=11, column=1, padx=5, pady=5)

        self.ipv4_button.grid(row=12, column=1, columnspan=2, pady=10)
        self.ipv6_button.grid(row=13, column=1, columnspan=2, pady=10)

    # Methode zur Berechnung von IPv4-Subnetzinformationen
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

    # Methode zur Berechnung von IPv6-Subnetzinformationen
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

    # Methode zur Überprüfung, ob eine gültige IPv4-Adresse eingegeben wurde
    def validate_ipv4(self, ip):
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    # Methode zur Überprüfung, ob eine gültige IPv6-Adresse eingegeben wurde
    def validate_ipv6(self, ip):
        try:
            ipaddress.IPv6Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    # Methode zur Anzeige von Fehlermeldungen in einem Popup-Fenster
    def show_error_message(self, message):
        messagebox.showerror("Fehler!", message)

if __name__ == "__main__":
    app = IPAddressCalculator()
    app.mainloop()
