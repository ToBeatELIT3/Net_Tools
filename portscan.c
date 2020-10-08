//ToBeatElite
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

void scanport(char *target_ip, int target_port, int server_socket) {
    struct sockaddr_in server_adress;
    server_adress.sin_family = AF_INET;
    server_adress.sin_port = htons(target_port); 
    server_adress.sin_addr.s_addr = *target_ip;

    int connection_status = connect(server_socket, (struct sockaddr *) &server_adress, sizeof(server_adress));

    if (connection_status == -1) {
	printf("Port # %i Is CLOSED\n", target_port);
    }

    else {
	printf("Port # %i is OPEN\n", target_port);
    }
}

int main(int argc, char* argv[]) {
    int tcp_client = socket(AF_INET, SOCK_STREAM, 0);

    if (tcp_client == -1) {
	printf("Error Creating Socket\n");
	return 0;
    }

    for (int i = 1; i < 1000; i++) {
	scanport(argv[1], i, tcp_client);
    }

    close(tcp_client);
    return 1;
}

