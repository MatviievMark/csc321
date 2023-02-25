import netifaces
import ipaddress
import pandas as pd


def get_interfaces():
    return netifaces.interfaces()


var = get_interfaces()


def goThroughInterfaces(interfaces):

    data = {
        'Adress': interfaces,
    }
    df = pd.DataFrame(data)
    print(df)


# ----------------------------------------------------------------
# get_mac retrieves the MAC adress of a given interface


def get_mac(interface: str):
    # get the adress for the given interface
    iface = netifaces.ifaddresses(interface)

    # check if the LINK constant is available
    if netifaces.AF_LINK in iface:
        # get the link info
        link_info = iface[netifaces.AF_LINK]

        # make sure there is a link and "addr" is avaliable
        if len(link_info) > 0 and 'addr' in link_info[0]:
            return link_info[0]['addr']

        # if not, return None
        return None


def goThroughMAC(interfaces):

    data = {
        'Adress': interfaces,
        'MAC': [get_mac(adress) for adress in interfaces]
    }
    df = pd.DataFrame(data)
    print(df)


# ----------------------------------------------------------------
# function that returns both the IPv4 and IPv6 addresses of a given interface as a dictioary object


def get_ips(interface: str):
    # create a dictioary object
    ip_adresses = dict()

    # get the adress info for the given interface
    iface = netifaces.ifaddresses(interface)

    # check if the AF_INET6 constant is available
    if netifaces.AF_INET6 in iface:
        # get the IPv6 info
        ipv6_info = iface[netifaces.AF_INET6]

        # make sure there is an IPv6 address and "addr" is available
        if len(ipv6_info) > 0 and 'addr' in ipv6_info[0]:
            # store the adress in the dictionary
            key = ipv6_info[0]['addr']
            value = 'IPv6'
            ip_adresses[key] = value

    # check if the AF_INET constant is available
    if netifaces.AF_INET in iface:
        # get the IPv4 info
        ipv4_info = iface[netifaces.AF_INET]

        # make sure there is an IPv4 address and "addr" is available
        if len(ipv4_info) > 0 and 'addr' in ipv4_info[0]:
            # store the adress in the dictiooary
            key = ipv4_info[0]['addr']
            value = 'IPv4'
            ip_adresses[key] = value

    return ip_adresses


def goThroughIPs(interfaces):

    data = {
        'Adress': interfaces,
        'ipv4 & ipv6': [get_ips(adress) for adress in interfaces]
    }
    df = pd.DataFrame(data)
    print(df)


# ----------------------------------------------------------------
# function that returns both the IPv4 adress and the IPv6 adress object representation
# of the netmasks for the given interface as a dictionary


def get_netmasks(interface: str):
    # create a dictioary object
    ip_adresses = dict()

    # get the adress info for the given interface
    iface = netifaces.ifaddresses(interface)

    # check if the AF_INET6 constant is available
    if netifaces.AF_INET6 in iface:
        # get the IPv6 info
        ipv6_info = iface[netifaces.AF_INET6]

        # make sure there is an IPv6 info and "netmask" is available
        if len(ipv6_info) > 0 and 'netmask' in ipv6_info[0]:
            # store the adress in the dictionary
            key = ipv6_info[0]['netmask']
            value = 'IPv6'
            ip_adresses[key] = value

    # check if the AF_INET constant is available
    if netifaces.AF_INET in iface:
        # get the IPv4 info
        ipv4_info = iface[netifaces.AF_INET]

        # make sure there is an IPv4 info and "netmask" is available
        if len(ipv4_info) > 0 and 'netmask' in ipv4_info[0]:
            # store the adress in the dictiooary
            key = ipv4_info[0]['netmask']
            value = 'IPv4'
            ip_adresses[key] = value

    return ip_adresses


def goThroughNetmasks(interfaces):

    data = {
        'Adress': interfaces,
        'ipv4 & ipv6': [get_netmasks(adress) for adress in interfaces]
    }
    df = pd.DataFrame(data)

    for index, row in df.iterrows():
        # get address information
        address_info = get_netmasks(row['Adress'])

        # get the list of ips associated with the address
        address_list = ','.join(
            [key+'/'+value for key, value in address_info.items()])

        # update the row with all netmask information
        df.loc[index, 'ipv4 & ipv6'] = address_list

    print(df)


# ----------------------------------------------------------------
# wrtie a unction that returns both the IPv4 and IPv6 objects as networks


def get_network(interface: str):
    # create a dictionary
    networks = dict()
    iface = netifaces.ifaddresses(interface)

    # check if the AF_INET6 constant is available
    if netifaces.AF_INET6 in iface:
        # get the IPv6 info and create IPv6Netwrok object
        ipv6_info = iface[netifaces.AF_INET6]
        key = ipv6_info[0]['addr']
        value = ipaddress.IPv6Network(key)
        networks["v6"] = value

    # check if the AF_INET constant is available
    if netifaces.AF_INET in iface:
        # get the IPv4 info and create IPv4Netwlrk object
        ipv4_info = iface[netifaces.AF_INET]
        key = ipv4_info[0]['addr']
        value = ipaddress.IPv4Network(key)
        networks["v4"] = value

    return networks


def goThroughNetworks(interfaces):

    data = {
        'Adress': interfaces,
        'ipv4 & ipv6': [get_network(adress) for adress in interfaces]
    }
    df = pd.DataFrame(data)

    for index, row in df.iterrows():
        # get address information
        address_info = get_netmasks(row['Adress'])

        # get the list of ips associated with the address
        address_list = ','.join(
            [key+'/'+value for key, value in address_info.items()])

        # update the row with all netmask information
        df.loc[index, 'ipv4 & ipv6'] = address_list

    print(df)


# def goThroughNetworks(interfaces):

#     data = {
#         'Adress': interfaces,
#         'ipv4 & ipv6': [get_network(adress) for adress in interfaces]
#     }
#     df = pd.DataFrame(data)
#     print(df)

# ----------------------------------------------------------------
# calling the functions

# goThroughInterfaces(var)
# goThroughMAC(var)
# goThroughIPs(var)
# goThroughNetmasks(var)
# goThroughNetworks(var)
