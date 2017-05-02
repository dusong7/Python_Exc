#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <iostream>

int writeFIFO(int in)
{
    const char *fifo_name = "/tmp/my_fifo";
    int pipe_fd = -1;
    int data_fd = -1;
    int res = 0;
    const int open_mode = O_WRONLY;
    int bytes_sent = 0;
    char buffer[PIPE_BUF + 1];
    int bytes_read = 0;

    if(access(fifo_name, F_OK) == -1)
    {
        printf ("Create the fifo pipe.\n");
        res = mkfifo(fifo_name, 0777);

        if(res != 0)
        {
            fprintf(stderr, "Could not create fifo %s\n", fifo_name);
            exit(EXIT_FAILURE);
        }
    }

    if(in != -1)
    {
        std::ofstream file;
        file.open("Data.txt");
        file<<in;
        file.close();
    }
    printf("Process %d opening FIFO O_WRONLY\n", getpid());
    pipe_fd = open(fifo_name, open_mode);
    printf("Process %d result %d\n", getpid(), pipe_fd);

    if(pipe_fd != -1)
    {
        bytes_read = 0;
        data_fd = open("Data.txt", O_RDONLY);
        if (data_fd == -1)
        {
            close(pipe_fd);
            fprintf (stderr, "Open file[Data.txt] failed\n");
            return -1;
        }

        bytes_read = read(data_fd, buffer, PIPE_BUF);
        buffer[bytes_read] = '\0';
        while(bytes_read > 0)
        {

            res = write(pipe_fd, buffer, bytes_read);
            if(res == -1)
            {
                fprintf(stderr, "Write error on pipe\n");
                exit(EXIT_FAILURE);
            }

            bytes_sent += res;
            bytes_read = read(data_fd, buffer, PIPE_BUF);
            buffer[bytes_read] = '\0';
        }

        close(pipe_fd);
        close(data_fd);
    }
    else
        exit(EXIT_FAILURE);

    printf("Process %d finished\n", getpid());
    return 1;
}

int main()
{
//    while(1)
//    {
//        writeFIFO(1);
//        usleep(1000*1000*1);
//    }
     int i = 0;
     while(1)
     {

         writeFIFO(i%2);
         i++;
         usleep(1000*1000*1);
     }

     return 0;
   // exit(EXIT_SUCCESS);
}

//Cli
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <limits.h>
#include <string.h>

int value()
{
    const char *fifo_name = "/tmp/my_fifo";
    int pipe_fd = -1;
    int data_fd = -1;
    int res = 0;
    int open_mode = O_RDONLY;
    char buffer[3 + 1];
    int bytes_read = 0;
    int bytes_write = 0;



    memset(buffer, '\0', sizeof(buffer));

    printf("Process %d opening FIFO O_RDONLY\n", getpid());
    pipe_fd = open(fifo_name, open_mode);
    data_fd = open("DataFormFIFO.txt", O_WRONLY|O_CREAT, 0644);


    if (data_fd == -1)
    {
        fprintf(stderr, "Open file[DataFormFIFO.txt] failed\n");
        close(pipe_fd);
        return -1;
    }

    printf("Process %d result %d\n",getpid(), pipe_fd);
    if(pipe_fd != -1)
    {
        do
        {
            res = read(pipe_fd, buffer, PIPE_BUF);
            bytes_write = write(data_fd, buffer, res);
            bytes_read += res;
        }while(res > 0);

        close(pipe_fd);
        close(data_fd);
    }
    else
        exit(EXIT_FAILURE);
//    printf("%s",buffer);
    printf("Process %d finished, %d bytes read\n", getpid(), bytes_read);
    if (buffer[0] == '1')
    {
        return 1;
    }
    else
    {
        return 0;
    }
//    exit(EXIT_SUCCESS);
}

int main()
{

    while(1)
    {
        int num = value();
        printf("%d_", num);
        usleep(1000*1000*1);
    }

}
