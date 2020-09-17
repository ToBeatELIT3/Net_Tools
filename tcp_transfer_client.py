#ToBeatElite
from tqdm import tqdm
import socket
import sys
import os

def connect(target_ip, target_port, file_to_send):
    file_size = os.path.getsize(file_to_send)

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.connect((target_ip, target_port))
    tcp_server.send(bytes(f"{file_to_send}<DIFF>{file_size}", "utf-8"))
    
    progress_bar = tqdm(range(file_size), f"Transferring {file_to_send}", unit="B", unit_scale=True, unit_divisor=4096)

    with open(file_to_send, "rb") as my_file:
        for x in progress_bar:
            bytes_read = my_file.read(4096)
            if not bytes_read: break
            tcp_server.sendall(bytes_read)
            progress_bar.update(len(bytes_read))

    tcp_server.close()
    
def main():
    try:
        my_target = sys.argv[1]
        my_target_port = int(sys.argv[2])
        my_file_to_send = sys.argv[3]

        connect(my_target, my_target_port, my_file_to_send)


    except Exception as ex: print(f"Usage: python {sys.argv[0]} [Target to Connect to] [Port to Connect to]\n{ex}")

if __name__ == "__main__": main()

