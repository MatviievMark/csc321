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
# import socket
# from ipaddress import ip_address
#
# #
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
import socket
#
# # Open the domains.tsv file and read the domain names
# with open('domains.tsv', 'r') as f:
#     domain_names = [line.split()[1] for line in f]
#
# # Loop through the domain names and get the reverse DNS for each domain
# results = []
# for domain in domain_names:
#     try:
#         ip = socket.gethostbyname(domain)
#         hostname = socket.gethostbyaddr(ip)[0]
#         result = (domain, hostname)
#     except socket.herror:
#         result = (domain, "No reverse DNS record found")
#     except socket.gaierror:
#         result = (domain, "Error resolving domain")
#     results.append(result)
#
# # Write the results to a new file called reverse_dns.txt
# with open('reverse_dns.txt', 'w') as f:
#     for result in results:
#         f.write(result[0] + '\t' + result[1] + '\n')


# -----------------------------------------------------------------
# prob 4



# Import necessary libraries
import socket
import dns.resolver
import dns.reversename
import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def read_domains_from_tsv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split('\t')[1] for line in lines]


def perform_reverse_dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        reversed_dns = dns.resolver.resolve(dns.reversename.from_address(ip_address), "PTR")
        return str(reversed_dns[0])[:-1]
    except Exception as e:
        print(f"Error performing reverse DNS lookup for {domain}: {e}")
        return None


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


if __name__ == "__main__":
    file_path = "domains.tsv"
    domains = read_domains_from_tsv(file_path)
    reverse_dns_lookup = {domain: perform_reverse_dns_lookup(domain) for domain in domains}

    G = nx.Graph()
    G.add_edges_from((domain, reverse_dns) for domain, reverse_dns in reverse_dns_lookup.items() if reverse_dns)

    visualize_graph(G)

#it displays a lot so im assuming its correct

