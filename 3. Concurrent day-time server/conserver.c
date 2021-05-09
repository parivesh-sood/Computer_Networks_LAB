#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>
int main()
{
            struct sockaddr_in sa;
            int sockfd, coontfd;
            char str[1025];
            time_t tick;
            sockfd = socket(AF_INET, SOCK_STREAM, 0);  
            if (sockfd < 0)
            {
                        printf("Error in creating socket\n");
                        exit(0);
            }
            else
            {
                        printf("Socket Created\n");
            }
            printf("Socket created\n");
            bzero(&sa, sizeof(sa));
    memset(str, '0', sizeof(str));
            sa.sin_family = AF_INET;
            sa.sin_port = htons(5600);
            sa.sin_addr.s_addr = htonl(INADDR_ANY);
            if (bind(sockfd, (struct sockaddr*)&sa, sizeof(sa))<0)
            {
                        printf("Bind Error\n");
            }
            else
                        printf("Binded\n");
            listen(sockfd, 10);
            while(1)
            {
                        coontfd = accept(sockfd, (struct sockaddr*)NULL ,NULL); 
                        printf("Accepted\n");
        tick = time(NULL);
        snprintf(str, sizeof(str), "%.24s\r\n", ctime(&tick));
        printf("sent\n");
        printf("%s\n", str);
                        write(coontfd, str, strlen(str)); // send buffer to client
            }
            close(sockfd); // close the socket
            return 0;
}
