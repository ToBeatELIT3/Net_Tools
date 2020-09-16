#ToBeatElite
from threading import Thread
import subprocess
import socket
import sys

def connect_on_socket(target_ip, target_port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.connect((target_ip, target_port))
    print("Type CLOSE to Close Connection\n" + tcp_server.recv(4096).decode("utf-8"))    

    while True:
        my_command = input("<NET>")
        tcp_server.send(bytes(my_command, "utf-8"))
        recived_data = tcp_server.recv(4096)
        print(recived_data.decode("utf-8"))

def main():
    try:
        my_target = sys.argv[1]
        my_target_port = int(sys.argv[2])
        connect_on_socket(my_target, my_target_port)

    except Exception as ex: print(f"Usage: python {sys.argv[0]} [Target to Connect to] [Port to Connect to]\n{ex}")

if __name__ == "__main__": main()

