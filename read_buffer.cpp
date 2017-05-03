   
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

   int main()
   {
    int bytes_read_ = 0;
    char buffer_[PIPE_BUF + 1];
    int data_fd = 4;
    data_fd = open("Data.txt", O_RDONLY);//"1234"
    int bytes_read = read(data_fd, buffer_, PIPE_BUF); //4
    int bytes_read__ = read(data_fd, buffer_, PIPE_BUF);//0
    return 0;
   }
   
