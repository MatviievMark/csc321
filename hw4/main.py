# prob 1
import csv
#
# with open("domains.tsv", "r") as file:
#     # Create a csv reader object with tab as delimiter
#     reader = csv.reader(file, delimiter="\t")
#     for row in reader:
#         # Get the site name from the first column
#         site = row[0]
#         # Split the site name by "." and get the last two parts
#         domain = ".".join(site.split(".")[-2:])
#         print(domain)

# -----------------------------------------------------------------
# prob 2
import socket
from ipaddress import ip_address

#
# with open('domains.tsv', 'r') as file:
#     # Read each line in the file
#     for line in file:
#         # Split the line by tabl charecters and extract the domain name
#         domain = line.split('\t')[1].strip()
#         try:
#             # Attempt to perform a forward DNS lookup for the domain name
#             ip_address = socket.gethostbyname(domain)
#             # print domain name and IP address
#             print(f'{domain}: {ip_address}')
#         except socket.gaierror:
#             # if lookup failed, print error
#             print(f'Error: Could not resolve {domain}')

# -----------------------------------------------------------------
# prob 3

# with open('domains.tsv') as file:
#     # read the file
#     for line in file:
#         # split the line
#         domain = line.split('\t')[1].strip()
#
#         try:
#             # forward DNS lookup for the domain name
#             ip_address = socket.getaddrinfo(domain, None)
#             # iterate through each IP address associated with the domain
#             for ip_address in ip_address:
#                 try:
#                     # reverse DNS lookup for the IP adress
#                     reverse_dns = socket.gethostbyaddr(ip_address[4][0])
#                     # print the IP and hostname
#                     print(f'f{ip_address[4][0]}: {reverse_dns[0]}')
#                 except socket.herror:
#                     print(f"Error: No reverse DNS record could be found for {ip_address[4][0]}")
#         except socket.gaierror:
#             # print error message
#             print(f'Error: Could not resolve {domain}')

# -----------------------------------------------------------------
# prob 4



# Import necessary libraries
import socket
import pandas as pd
import dns.resolver
import dns.reversename
import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# Function to read domains from the TSV file
def read_domains_from_tsv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    domains = [line.strip().split('\t')[0] for line in lines]
    return domains


# Function to perform reverse DNS lookup for a given domain
def perform_reverse_dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        reversed_dns = dns.resolver.resolve(dns.reversename.from_address(ip_address), "PTR")
        return str(reversed_dns[0])[:-1]
    except Exception as e:
        print(f"Error performing reverse DNS lookup for {domain}: {e}")
        return None


# Read domains from TSV file and perform reverse DNS lookup
file_path = "domains.tsv"
domains = read_domains_from_tsv(file_path)
reverse_dns_lookup = {domain: perform_reverse_dns_lookup(domain) for domain in domains}


# Function to visualize the graph using Tkinter
def visualize_graph(graph):
    root = tk.Tk()
    root.title("Domains Graph")

    figure = plt.Figure(figsize=(12, 6), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, ax=ax, with_labels=True, font_size=8, node_size=500, node_color="skyblue", edge_color="gray", font_color="black")
    ax.set_title("Domains and Reverse DNS Lookups")
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

    root.mainloop()


# Create a graph and populate it with domain and reverse DNS data
G = nx.Graph()
for domain, reverse_dns in reverse_dns_lookup.items():
    if reverse_dns:
        G.add_edge(domain, reverse_dns)

# Visualize the graph using Tkinter
visualize_graph(G)

# I don't know why but nothing exists so yeah i had to make it with
# tk inter because I thought it kept making mistakes but actually there was
# just nothing
