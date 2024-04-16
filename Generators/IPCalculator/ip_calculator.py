import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress
from ipv4_calculator import calculate_ipv4
from ipv6_calculator import calculate_ipv6
import validators

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
