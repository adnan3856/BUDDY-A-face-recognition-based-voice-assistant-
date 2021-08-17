import socket

hostname = socket.gethostname()
def find_ip():
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr
