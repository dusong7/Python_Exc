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
using namespace std;

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
//   int i = 0;
//   for(i= 0; i<100000;i++)
//   {
//     if(getch() == 'E')
//     {
//        break;
//     }
//   }
  char str1[30], str2[30];

   cin.get(str1, 30);

   cin.get();

   cin.get(str2, 30);

   cout << "str1: " << str1 << endl;

   cout << "str2: " << str2 << endl;
   return 0;
}





目录(?)[+]
1.cin

C++ 使用cin可以方便的读取键盘输入的字符，例如：
[cpp] view plain copy

    //test input  
    #include <iostream>                             
    int main()                                
    {                                         
        using namespace std;  
        const int size = 20;  
        char name[size];  
        char pl[size];//program language  
      
        cout<<"Enter your name:";  
        cin>>name;  
        cout<<"Enter your favorite program language:";  
        cin>>pl;  
        cout<<"Hello "<<name<<", your favorite program language is "<<pl<<endl;  
        return 0;  
    }  


首先，每个输入我们只输入一个单词，如下：

但如果我们在第一个输入时填写两个以上单词：

可以发现，第二个输入还没来得及响应，就已经都显示出来了。

原因是：cin通过使用空白（空格、制表符和换行符）来定字符串的界。这意味着cin在读取字符数组输入时只读取一个单词，读取该单词后，cin将该字符串放一数组中，并自动结尾添加空字符。另外，cin也没有很好的控件输入的字符数，即输入字符数大于数组大小的情况没有处理。
2.cin.getline()

基于上面的情况，使用cin.getline()读取一行数据。

cin.getline()函数读取整行，它使用通过回车键输入的换行符来确定输入结尾。该函数有两个参数。第一个参数是用来存储输入行的数组的名称，第二个参数是要读取的字符数（包括空字符），cin.getline()成员函数在读取指定数目的字符或遇到换行符时停止读取

如下：
[cpp] view plain copy

    cout<<"Enter your name:";  
    cin.getline(name,size);  
    cout<<"Enter your favorite program language:";  
    cin.getline(pl,size);  
    cout<<"Hello "<<name<<", your favorite program language is "<<pl<<endl;  

现在再来获得多个单词的输入：

发现就正常了。需要注意的是，cin.getline()丢弃了换行符。
3.cin.get()

get()函数有好几种变体，其中有一种与getline()完全相同的参数，但该函数不再读取并丢弃换行符(不读取意味着换行符还在输入队列中)：
[cpp] view plain copy

    cout<<"Enter your name:";  
    cin.get(name,size);  
    cout<<"Enter your favorite program language:";  
    cin.get(pl,size);  
    cout<<"Hello "<<name<<", your favorite program language is "<<pl<<endl;  

尝试输入：

发现并不好使，原因是由于第一次调用后，换行符将留存输入队列中，因此第二次调用时看到的第一个字符为换行符。因此get认为已经到达行尾，而没有发现任何可读取的内容。get()（不带任何参数的变体）可以读取下一个字符（包括换行符）。因此可以：
[cpp] view plain copy

    cin.get(name,size).get();  
    cin.get(pl,size).get();  

即可。

注意：有些C++版本没有不带参数的get()变体。可能有只有char参数的变体。可用下面的代替：

char ch;cin.get(name,size).get(ch);
4.读取空行和其他问题

当getline()或get()读取空行时将如何？一般是下一条输入语句将在前一条结束读取的位置开始读取；但当有空行时，当get()读取空行后将设置失效位(failbit)，这意味接下来的输入将被阻断，但可以用下面的命令来恢复输入：cin.clear()    cout<<"Enter your name:";  
[cpp] view plain copy

    cout<<"Enter your name:";    
    cin.get(name,size).get();    
    if (!cin)  
    {  
        cin.clear();  
        while (cin.get()!='\n')  
        {  
            continue;  
        }  
    }  
    cout<<"Enter your favorite program language:";    
    cin.get(pl,size).get();    
    cout<<"Hello "<<name<<", your favorite program language is "<<pl<<endl;  

另一个潜在的问题是，输入字符可能比分配的空间长。如果输入行包含的字符数比指定的多，则这get()和getline()将把余下的字符留在输入队列中，而getline()还会设置失效位，并关闭输入。

[cpp] view plain copy

    cout<<"Enter your name:";    
    cin.getline(name,size);    
    if (!cin)  
    {  
        cin.clear();  
        while (cin.get()!='\n')  
        {  
            continue;  
        }  
    }  
    cout<<"Enter your favorite program language:";    
    cin.getline(pl,size);    
    cout<<"Hello "<<name<<", your favorite program language is "<<pl<<endl  

5.混合输入字符串和数字

[cpp] view plain copy

    int age = 0;  
    char address[size] = {0};  
      
    cout<<"Enter your age:";  
    cin>>age;  
    cout<<"Enter your address:";  
    cin.getline(address,size);  
    cout<<"your age is "<<age <<", your address is "<<address<<endl;  

上面的写法有问题，会导致第二个输入没有机会。原因是：当cin读取年龄时，将回车键生成的换行符留存了输入队列中，后面的cin.getline()看到换行符后，将认为是一个空行，并将一个空字符串赋给address数组。解决办法为在cin>>age;后加cin.get();




  

目录(?)[+]
1.scanf

charstr[15];

scanf("%s",str);

abc 123 

1)      不读入空格和回车,从空格处结束

2)      输入字符串长度超过字符数组元素个数不报错

3)      当输入项为字符指针时，指针必须已指向确定的有足够空间的连续存储单元 

4)      当为数组元素地址时，从此元素地址开始存放

printf("%s",地址值)

输出时遇到第一个'\0'为止
2.gets和puts函数

开头必须stdio.h;

Gets输入时包括空格符，遇到回车结束

Puts遇到第一个‘\0’结束，自动加入换行符
3.fgets

而使用fgets函数时，只要第二个参数正好等于第一个参数传给它的数组的字节个数，那么fgets函数不会写出数组边界。所以，fgets函数是最好的选择。

fgets(...)读入文本行时的两种情况。

1).如果n大于一行的字符串长度，那么当读到字符串末尾的换行符时，fgets(..)会返回。并且在s的最后插入字符串结束标志'\0'。而s缓冲区剩余的位置不会再填充。

          example：

              123abc

              fgets(s,10,fp);

              此时，读入七个字符，123abc\n,实际上还有最后的'\0',所以，strlen(s)=7;如果要去除末尾的\n，s[strlen(s)-1]='\0';便可。

2).    如果n小于等于一行的字符串的长度，那么读入n-1个字符，此时并没有读入\n因为并没有到行尾，同样在最后会插入'\0'.

         example:

           123abc

           char  s[5];

           fgets(s,5,fp);

           这时读入4个字符，123a,并没有换行符，所以strlen(s)=4.
4.cin

使用空白（空格，制表符和换行符）来定字符串的界的
5.getline()

读入整行数据，它使用回车键输入的换行符来确定输入结尾。

调用方法: cin.getline(str, len);

第一个参数str是用来存储输入行的数组名称，第二个参数len是要读取的字符数。
6.get()

调用方法：cin.get(str, len);

getline将丢弃换行符，而get()将换行符保留在输入序列里，但是字符串中并没有换行符。

使用cin.get()输入多行数据时，中间可以使用get()消除换行符。

 

int main()

{

   char str1[30], str2[30];

   cin.get(str1, 30);

   cin.get();

   cin.get(str2, 30);

   cout << "str1: " << str1 << endl;

   cout << "str2: " << str2 << endl;

   return 0;

}
