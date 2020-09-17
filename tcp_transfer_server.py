#ToBeatElite
from tqdm import tqdm
import socket
import sys
import os

def listen(target_ip, target_port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((target_ip, target_port))
    tcp_server.listen(5)

    print(f"Listening on {socket.gethostname()} : {target_port}")
    client_socket, client_address = tcp_server.accept()
    print(f"Connection from {client_address} has been Established")

    recived_data = client_socket.recv(4096).decode("utf-8")
    filename, filesize = recived_data.split("<DIFF>")

    filesize = int(filesize)
    filename = os.path.basename(filename)
    
    progress_bar = tqdm(range(filesize), f"Recieving {filename}", unit="B", unit_scale=True, unit_divisor=4096)
    
    with open(filename, "wb") as my_file:
        for x in progress_bar:
            bytes_read = client_socket.recv(4096)
            if not bytes_read: break
            my_file.write(bytes_read)
            progress_bar.update(len(bytes_read))

    tcp_server.close()
    main()

def main():
    try:
        my_target = sys.argv[1]
        my_target_port = int(sys.argv[2])

        listen(my_target, my_target_port)

    except Exception as ex: print(f"Usage: python {sys.argv[0]} [Target to Connect to] [Port to Connect to]\n{ex}")

if __name__ == "__main__": main()
