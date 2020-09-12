#ToBeatElite
import socket
import sys

def connect(target_ip, target_port, data_to_send):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_server.sendto(bytes(data_to_send, "utf-8"))
    
    try:
        recived_data = tcp_server.recvfrom(4096)
        print(recived_data.decode("utf-8"))

    except: print("No Data Recieved")

def main():
    try:
        my_target = sys.argv[1]
        my_target_port = int(sys.argv[2])
        my_data = str(sys.argv[3])
        connect(my_target, my_target_port, my_data)

    except Exception as ex:
        print(f"Usage: python {sys.argv[0]} [Target to Connect to] [Port to Connect to] [Data to Send]\n{ex}")

if __name__ == "__main__": main()

