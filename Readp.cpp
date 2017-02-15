#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <fstream>
#include <thread>
#include <vector>

using namespace std;


struct SAngle
{
	short Angle[3];
	short T;
};

enum Datatype{Angle_acce, Acce};

struct SAngle stcAngle;

std::ofstream out("//home/admini/Documents/fileTest");

void set_speed(int fd, int speed)
{
    int speed_arr[] = {B115200,B38400, B19200, B9600, B4800, B2400, B1200, B300 };
    int name_arr[] = {115200,38400, 19200, 9600, 4800, 2400, 1200, 300 };

    int   i;
    int   status;
    struct termios   Opt;    //串口相关的结构体
    tcgetattr(fd, &Opt);    //保存原有的串口配置，保存在Opt中
    for ( i= 0; i < sizeof(speed_arr) / sizeof(int); i++)
    {
        /* 输入参数为115200，转换为B115200,termios结构体中使用B115200*/
        if (speed == name_arr[i])
        {
            tcflush(fd, TCIOFLUSH);  //刷清输入、输出队列
            //cfsetispeed(&Opt, speed_arr[i]);//设置输入波特率
            cfsetospeed(&Opt, speed_arr[i]);//设置输出波特率
            status = tcsetattr(fd, TCSANOW, &Opt);//更改设置立即生效

            if (status != 0)
            {
                perror("tcsetattr fd1 error");
                return;
            }
            else
            {
               // printf("set fd1 ok \n");
            }

            tcflush(fd,TCIOFLUSH); //刷清输入、输出队列
            }
    }
}

int OpenPort()
{
    int fd,flag,rd_num=0;
    struct termios term;//定义一结构体
    speed_t baud_rate_i,baud_rate_o,baud_rate_a,baud_rate_b;    //定义波特率
    char recv_buf[20];//读写使用的数组，发送，接收两种数组
    //fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK|O_NOCTTY | O_NDELAY);     //打开设备文件，使用USB转串口，设备文件为/dev/ttyUSB0 O_NOCTTY | O_NDELAY
    fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK);
    if(fd==-1)    //error
        printf("can not open the ttyUSB0!\n");
    else
        return fd;
       //ok
       // printf("open USB-Serial ttyUSB0 ok!\n");

    flag=tcgetattr(fd,&term);
    baud_rate_i=cfgetispeed(&term);
    baud_rate_o=cfgetospeed(&term);
    //printf("baudrate of in is:%d,baudrate of out is%d,fd=%d\n",baud_rate_i,baud_rate_o,fd);/*打印设置之前的波特率，目的是方便和设置之后的波特率对比*/

    set_speed(fd,9600);/*重新设置波特率*/
    /* tcgetattr 与 tcgetattr成功时返回0  */
    flag=tcgetattr(fd,&term);/*以下三行读取设置之后的波特率，用cfgetispeed和cfgetospeed得到的波特率是一个序号，可以通过查表（表见程序后面）得到真正的波特率，比如返回13，对应的实际波特率是9600。我这里没有做转换，直接把13输出了。*/
    baud_rate_a=cfgetispeed(&term);/*设置输入波特率*/
    baud_rate_b=cfgetospeed(&term);/*设置输出波特率*/
}

void getData(int fd, Datatype dt, float &val1, float &val2, float &val3)
{
    char recv_buf[20];//读写使用的数组，发送，接收两种数组
    //
    int rd_num;

    while(1)
    {
        read(fd,recv_buf,11);
        if(recv_buf[0] == 0x55)
        {
        //    printf("get data\n");

            break;
        }
      //  printf("cur %x\n", recv_buf[0]);
    }

    while(1)
    {
        rd_num=read(fd,recv_buf,11);/*再读出*//*返回值是真正读出了多少个字符*/

//        printf("%x_%x_%d\n", recv_buf[0], recv_buf[1], rd_num);
        if(rd_num>0)
        {
            if(recv_buf[1] == 0x52 && dt==Angle_acce)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2] & 0xff);
				stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4] & 0xff);
				stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6] & 0xff);

                //printf("Angle_Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*2000,(float)stcAngle.Angle[1]/32768*2000,(float)stcAngle.Angle[2]/32768*2000);
                val1 = (float)stcAngle.Angle[0]/32768*2000;
                val2 = (float)stcAngle.Angle[1]/32768*2000;
                val3 = (float)stcAngle.Angle[2]/32768*2000;
                return;
            }

             if(recv_buf[1] == 0x51 && dt == Acce)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2]);
				stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4]);
				stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6]);

                //printf("Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*16,(float)stcAngle.Angle[1]/32768*16,(float)stcAngle.Angle[2]/32768*16);

                val1 = (float)stcAngle.Angle[0]/32768*16 *9.8;
                val2 = (float)stcAngle.Angle[1]/32768*16 *9.8;
                val3 = (float)stcAngle.Angle[2]/32768*16 *9.8;

                return;
            }

        }

//            printf("read ttyUSB0 fail!\n");
        usleep(21500); //

    }
}

void getImuData(Datatype dt, float &val1, float &val2, float &val3)
{
    int fd,flag,rd_num=0;
    struct termios term;//定义一结构体
    speed_t baud_rate_i,baud_rate_o,baud_rate_a,baud_rate_b;    //定义波特率
    char recv_buf[20];//读写使用的数组，发送，接收两种数组
    //fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK|O_NOCTTY | O_NDELAY);     //打开设备文件，使用USB转串口，设备文件为/dev/ttyUSB0 O_NOCTTY | O_NDELAY
    fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK);
    if(fd==-1)    //error
        printf("can not open the ttyUSB0!\n");
    else    //ok
       // printf("open USB-Serial ttyUSB0 ok!\n");

    flag=tcgetattr(fd,&term);
    baud_rate_i=cfgetispeed(&term);
    baud_rate_o=cfgetospeed(&term);
    //printf("baudrate of in is:%d,baudrate of out is%d,fd=%d\n",baud_rate_i,baud_rate_o,fd);/*打印设置之前的波特率，目的是方便和设置之后的波特率对比*/

    set_speed(fd,9600);/*重新设置波特率*/
    /* tcgetattr 与 tcgetattr成功时返回0  */
    flag=tcgetattr(fd,&term);/*以下三行读取设置之后的波特率，用cfgetispeed和cfgetospeed得到的波特率是一个序号，可以通过查表（表见程序后面）得到真正的波特率，比如返回13，对应的实际波特率是9600。我这里没有做转换，直接把13输出了。*/
    baud_rate_a=cfgetispeed(&term);/*设置输入波特率*/
    baud_rate_b=cfgetospeed(&term);/*设置输出波特率*/
   // printf("baudrate of in is:%d,baudrate of out is%d,fd=%d,flag=%d\n,",baud_rate_a,baud_rate_b,fd,flag);/*打印设置之后的波特率，目的是方便和设置之后的波特率对比*/

    while(1)
    {
        read(fd,recv_buf,11);
        if(recv_buf[0] == 0x55)
        {
        //    printf("get data\n");

            break;
        }
      //  printf("cur %x\n", recv_buf[0]);
    }

    while(1)
    {
        rd_num=read(fd,recv_buf,11);/*再读出*//*返回值是真正读出了多少个字符*/

//        printf("%x_%x_%d\n", recv_buf[0], recv_buf[1], rd_num);
        if(rd_num>0)
        {
            if(recv_buf[1] == 0x52 && dt==Angle_acce)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2] & 0xff);
				stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4] & 0xff);
				stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6] & 0xff);

                //printf("Angle_Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*2000,(float)stcAngle.Angle[1]/32768*2000,(float)stcAngle.Angle[2]/32768*2000);
                val1 = (float)stcAngle.Angle[0]/32768*2000;
                val2 = (float)stcAngle.Angle[1]/32768*2000;
                val3 = (float)stcAngle.Angle[2]/32768*2000;
                return;
            }

             if(recv_buf[1] == 0x51 && dt==Acce)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2]);
				stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4]);
				stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6]);

                //printf("Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*16,(float)stcAngle.Angle[1]/32768*16,(float)stcAngle.Angle[2]/32768*16);

                val1 = (float)stcAngle.Angle[0]/32768*16 *9.8;
                val2 = (float)stcAngle.Angle[1]/32768*16 *9.8;
                val3 = (float)stcAngle.Angle[2]/32768*16 *9.8;

                return;
            }

        }

//            printf("read ttyUSB0 fail!\n");
        usleep(20000); //

    }
}


int main()
{
//    cout << "Hello world!" << endl;
    float val1, val2, val3;

    int fd = OpenPort();


    for(int i=0; i<10000;i++)
    {
//        getImuData(Angle_acce, val1, val2, val3);
//        cout<<val1<<" "<<val2<<" "<<val3<<endl;
//        out<<val1<<" "<<val2<<" "<<val3<<endl;
//        getImuData(Acce, val1, val2, val3);
//        cout<<val1<<" "<<val2<<" "<<val3<<endl;
        getData(fd,Angle_acce,val1, val2, val3);
        //cout<<val1<<" "<<val2<<" "<<val3<<endl;

        getData(fd,Acce,val1, val2, val3);
        cout<<val1<<" "<<val2<<" "<<val3<<endl;

        cout<<endl;
    }

    return 0;
}
