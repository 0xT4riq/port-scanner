import pyfiglet
import sys
import socket
import threading
import datetime 
import ipaddress
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

ascii_banner = pyfiglet.figlet_format("Port Scanner",font="epic")
print(ascii_banner)
print("_" * 60)
info_banner = pyfiglet.figlet_format("by 0xT4riq",font="term")
info_banner += "\nGitHub: https://github.com/0xT4riq\nVersion: 1.0\n\nUse responsibly. Unauthorized scanning is illegal.\n"
print(info_banner)
print("_" * 60)



target = input(str("Enter the target IP: "))
open_ports = []
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.error:
        print("Could not connect to server. Please check the target IP.")
        sys.exit()





def main():

    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Invalid IP address format. Please enter a valid IP address.")
        sys.exit()

    print("-" * 60)
    print("Scanning target: " + target)
    print("Scanning started at: " + str(datetime.datetime.now()))


    start_port = int(input("Enter the starting port (or -1 for all): "))
    if start_port < 0:
        start_port = 1
        end_port = 65535
    else:
        end_port = int(input("Enter the ending port: "))
    ports = list(range(start_port, end_port ))
    with ThreadPoolExecutor(max_workers=100) as executor:
        list(tqdm(executor.map(scan_port, ports), total=len(ports)))
    print("\nOpen ports:")
    for port in sorted(open_ports):
        print(port)

main()