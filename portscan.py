#ToBeatElite
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
from common_ports import common_tcp_ports, common_udp_ports
import multiprocessing
import time
import sys

open_ports = []

def scan(target_ip, target_port):
    try:
        target = gethostbyname(target_ip)
        connection = socket(AF_INET, SOCK_STREAM)

        scan_result = connection.connect_ex((target, target_port))

        if not scan_result:
            open_ports.append(target_port)
            print(f"Port # {target_port} is OPEN")

        else: print(f"Port # {target_port} is CLOSED")

    except Exception as e: print(e)

def threaded_scan(target_ip, target_port, time_per_scan):
    process = multiprocessing.Process(target=scan, args=(target_ip, target_port))
    process.start()
    process.join(time_per_scan)

    if process.is_alive(): process.terminate()

def main():
    try:
        
        fast_scan = False

        my_target = gethostbyname(sys.argv[1])

        if sys.argv[2] not in ["--all", "--common_udp", "--common_tcp"]: my_target_port = int(sys.argv[2])
        else: my_target_port = sys.argv[2]

        if sys.argv[3] != "--fast": my_time_limit = round(float(sys.argv[3]))
        else: fast_scan = True

        starting_time = time.time()

        if fast_scan:
            if my_target_port == "--all":
                for x in range(65535): scan(my_target, x)

            elif my_target_port == "--common_udp":
                for x in range(len(common_udp_ports)): scan(my_target, common_udp_ports[x])
            
                elif my_target_port == "--common_tcp":
                    for x in range(len(common_tcp_ports)): scan(my_target, common_tcp_ports[x])

            else: scan(my_target, my_target_port)

        else:
            if my_target_port == "--all":
                for x in range(65535): threaded_scan(my_target, x, my_time_limit)

            elif my_target_port == "--common":
                for x in range(len(common_port_list)): threaded_scan(my_target, common_port_list[x], my_time_limit)

            else: threaded_scan(my_target, my_target_port, my_time_limit)

        ending_time = time.time()
        
        if fast_scan: print("---OPEN_PORTS---")

        for x in range(len(open_ports)): print(f"Port # {open_ports[x]} is OPEN")
        print(f"Total Time : {starting_time - ending_time} Seconds")
    
    except Exception as e:
        print(f"\nUsage: python {sys.argv[0]} [target_ip] [--all] or [--common] or [target_port] [allocated_seconds_per_scan] or [--fast](experimental)]\n")
        print(e)
    

if __name__ == "__main__": main()
