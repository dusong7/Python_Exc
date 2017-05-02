//#include <unistd.h>
//#include <stdlib.h>
//#include <stdio.h>
//#include <fcntl.h>
//#include <sys/types.h>
//#include <sys/stat.h>
//#include <limits.h>
//#include <string.h>
//
//int value()
//{
//    const char *fifo_name = "/tmp/my_fifo";
//    int pipe_fd = -1;
//    int data_fd = -1;
//    int res = 0;
//    int open_mode = O_RDONLY;
//    char buffer[3 + 1];
//    int bytes_read = 0;
//    int bytes_write = 0;
//
//
//
//    memset(buffer, '\0', sizeof(buffer));
//
//    printf("Process %d opening FIFO O_RDONLY\n", getpid());
//    pipe_fd = open(fifo_name, open_mode);
//    data_fd = open("DataFormFIFO.txt", O_WRONLY|O_CREAT, 0644);
//
//
//    if (data_fd == -1)
//    {
//        fprintf(stderr, "Open file[DataFormFIFO.txt] failed\n");
//        close(pipe_fd);
//        return -1;
//    }
//
//    printf("Process %d result %d\n",getpid(), pipe_fd);
//    if(pipe_fd != -1)
//    {
//        do
//        {
//            res = read(pipe_fd, buffer, PIPE_BUF);
//            bytes_write = write(data_fd, buffer, res);
//            bytes_read += res;
//        }while(res > 0);
//
//        close(pipe_fd);
//        close(data_fd);
//    }
//    else
//        exit(EXIT_FAILURE);
////    printf("%s",buffer);
//    printf("Process %d finished, %d bytes read\n", getpid(), bytes_read);
//    if (buffer[0] == '1')
//    {
//        return 1;
//    }
//    else
//    {
//        return 0;
//    }
////    exit(EXIT_SUCCESS);
//}
////
//int main()
//{
//
//    while(1)
//    {
//        int num = value();
//        printf("%d_", num);
//        usleep(1000*1000*1);
//    }
//
//}
//////#include <stdio.h>
//////#include <stdlib.h>
//////#include <zconf.h>
//////#include <iostream>
//////#include <string.h>
//////#include <unistd.h>
//////#include <sys/ioctl.h>
//////#include <termios.h>
//////
//////bool isRun = false;
//////
//////bool isFileModified()
//////{
//////    //TODO:
//////    printf("Info");
//////    return false;
//////}
//////
//////int main()
//////{
////////
////////    FILE *file;
////////    file = fopen("file","w");
////////    fwrite("0",1,1,file);
////////    fclose(file);
//////
////////    while(1)
////////    {
////////        isFileModified();
////////        usleep(1000*100);
////////    }
//////////
////////    char input = '\0';
////////    while(input != 'E')
////////    {
//////////        scanf("%c", &input);
//////////
//////////        printf("%c", input);
////////        std::cin.get()>>input;
////////    }
////////    isFileModified();
//////    while (1)
//////    {
//////        printf("%c", getche());
////////        usleep(1000*1000);
//////    }
//////    return 0;
//////}
//////
//////#include <termio.h>
//////#include <cstdio>
//////#include <iostream>
//////#include <csignal>
//////
//////int getch(void)
//////{
//////    struct termios tm, tm_old;
//////    int fd = 0, ch;
//////
//////    if (tcgetattr(fd, &tm) < 0) {//保存现在的终端设置
//////        return -1;
//////    }
//////
//////    tm_old = tm;
//////    cfmakeraw(&tm);//更改终端设置为原始模式，该模式下所有的输入数据以字节为单位被处理
//////    if (tcsetattr(fd, TCSANOW, &tm) < 0) {//设置上更改之后的设置
//////        return -1;
//////    }
//////
//////    ch = getchar();
//////    if (tcsetattr(fd, TCSANOW, &tm_old) < 0) {//更改设置为最初的样子
//////        return -1;
//////    }
//////    return ch;
//////}
//////
//////int main()
//////{
//////    while (1)
//////    {
//////        if (getch() == ' ')
//////        {
//////            printf("W");
//////        }
//////
//////    }
//////
//////    return 0;
//////}
////
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include  <stdio.h>
#include  <stdlib.h>
#include <zconf.h>


using namespace std;


bool  isModify()
{
    //
    FILE *file;
    file = fopen("file","r");
    char str[2];
    fread(str,2,2,file);

    printf("%c",str[0]);

    return false;
}

bool fileWrite(bool bl)
{
    FILE *file;
    char *string1;
    if (bl)
    {
//        string1 = "1";
        memset(string1,0,0);
        file = fopen("1","w");
        if (access("file",0))
        {
            remove("file");
        }
    }
    else
    {
//        string1 = "0";
        memset(string1,0,1);
        file = fopen("0","w");
        if (access("file",0))
        {
            remove("file");
        }
    }
//    FILE *file;
//    file = fopen("file","w");
//    fwrite(string1,1,1,file);
    fclose(file);
}

int main()
{
    //
    fileWrite(false);
//    isModify();
    return 0;
}
