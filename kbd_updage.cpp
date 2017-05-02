//#include <unistd.h>
//#include <stdlib.h>
//#include <fcntl.h>
//#include <limits.h>
//#include <sys/types.h>
//#include <sys/stat.h>
//#include <stdio.h>
//#include <string.h>
//#include <fstream>
//#include <iostream>
//
//int writeFIFO(int in)
//{
//    const char *fifo_name = "/tmp/my_fifo";
//    int pipe_fd = -1;
//    int data_fd = -1;
//    int res = 0;
//    const int open_mode = O_WRONLY;
//    int bytes_sent = 0;
//    char buffer[PIPE_BUF + 1];
//    int bytes_read = 0;
//
//    if(access(fifo_name, F_OK) == -1)
//    {
//        printf ("Create the fifo pipe.\n");
//        res = mkfifo(fifo_name, 0777);
//
//        if(res != 0)
//        {
//            fprintf(stderr, "Could not create fifo %s\n", fifo_name);
//            exit(EXIT_FAILURE);
//        }
//    }
//
//    if(in != -1)
//    {
//        std::ofstream file;
//        file.open("Data.txt");
//        file<<in;
//        file.close();
//    }
//
//    printf("Process %d opening FIFO O_WRONLY\n", getpid());
//    pipe_fd = open(fifo_name, open_mode);
//    printf("Process %d result %d\n", getpid(), pipe_fd);
//
//    if(pipe_fd != -1)
//    {
//        bytes_read = 0;
//        data_fd = open("Data.txt", O_RDONLY);
//        if (data_fd == -1)
//        {
//            close(pipe_fd);
//            fprintf (stderr, "Open file[Data.txt] failed\n");
//            return -1;
//        }
//
//        bytes_read = read(data_fd, buffer, PIPE_BUF);
//        buffer[bytes_read] = '\0';
//        while(bytes_read > 0)
//        {
//
//            res = write(pipe_fd, buffer, bytes_read);
//            if(res == -1)
//            {
//                fprintf(stderr, "Write error on pipe\n");
//                exit(EXIT_FAILURE);
//            }
//
//            bytes_sent += res;
//            bytes_read = read(data_fd, buffer, PIPE_BUF);
//            buffer[bytes_read] = '\0';
//        }
//
//        close(pipe_fd);
//        close(data_fd);
//    }
//    else
//        exit(EXIT_FAILURE);
//
//    printf("Process %d finished\n", getpid());
//    return 1;
//}
//
//int main()
//{
////    while(1)
////    {
////        writeFIFO(1);
////        usleep(1000*1000*1);
////    }
////     int i = 0;
////     while(1)
////     {
////
////         writeFIFO(i%2);
////         i++;
////         usleep(1000*1000*1);
////     }
//while(1)
//{
//    writeFIFO(0);
//    usleep(1000*100);
//}
//
//     return 0;
//   // exit(EXIT_SUCCESS);
//}

#include <termio.h>
#include <cstdio>
#include <iostream>
#include <csignal>
#include <stdio.h>
#include <stdlib.h>


using namespace std;

void sighandle(int sig)
{
     printf("捕获到信号%d", sig);
     /*释放资源*/
      exit(0);
}

int getch(void)
{
    struct termios tm, tm_old;
    int fd = 0, ch;

    if (tcgetattr(fd, &tm) < 0) {//保存现在的终端设置
        return -1;
    }

    tm_old = tm;
    cfmakeraw(&tm);//更改终端设置为原始模式，该模式下所有的输入数据以字节为单位被处理
    if (tcsetattr(fd, TCSANOW, &tm) < 0) {//设置上更改之后的设置
        return -1;
    }

    ch = getchar();
    if (tcsetattr(fd, TCSANOW, &tm_old) < 0) {//更改设置为最初的样子
        return -1;
    }

    return ch;
}
char input='\0';
int main()
{
   //
    //signal(SIGINT, sighandle);  //设置信号处理函数
   int i = 0;
   for(i= 0; i<100000;i++)
   {

     char ch = getch();
     if( ch == 'E')
     {
        break;
     }
     else
     {
        switch(ch){
        case ' ':
            printf("W");
         break;
        case 'a':
            printf("A");
         break;
        case 's':
            printf("S");
         break;
        case 'd':
            printf("D");
         break;
         default:
         break;
         exit(EXIT_SUCCESS);
        }
     }

   }

//   char str1[30];
//
//   cin.get(str1, 30);


//   cout << "str1: " << str1 << endl;
//
//   cout << "str2: " << str2 << endl;
   return 0;
}
