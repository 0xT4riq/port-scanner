import pyfiglet
import sys
import socket
import threading
import datetime 


ascii_banner = pyfiglet.figlet_format("Port Scanner",font="epic")
print(ascii_banner)
print("_" * 60)
info_banner = pyfiglet.figlet_format("by 0xT4riq",font="straight")
info_banner += "\nGitHub: https://github.com/0xT4riq\nVersion: 1.0\n\nUse responsibly. Unauthorized scanning is illegal.\n"
print(info_banner)
print("_" * 60)


targer = input(str("Enter the target IP: "))
print("-" * 60)
print("Scanning target: " + targer)
print("Scanning started at: " + str(datetime.datetime.now()))

try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((targer, port))
        if result == 0:
            print(f"Port {port} is open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.error:
    print("Could not connect to server. Please check the target IP.")
    sys.exit()
