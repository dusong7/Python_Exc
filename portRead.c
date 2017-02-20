#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
struct SAngle
{
	short Angle[3];
	short T;
};

struct SAngle stcAngle={0};

void set_speed(int fd, int speed)
{
    int speed_arr[] = {B115200,B38400, B19200, B9600, B4800, B2400, B1200, B300 };
    int name_arr[] = {115200,38400, 19200, 9600, 4800, 2400, 1200, 300 };

    int   i;
    int   status;
    struct termios   Opt;    //Ž®¿ÚÏà¹ØµÄœá¹¹Ìå
    tcgetattr(fd, &Opt);    //±£ŽæÔ­ÓÐµÄŽ®¿ÚÅäÖÃ£¬±£ŽæÔÚOptÖÐ
    for ( i= 0; i < sizeof(speed_arr) / sizeof(int); i++)
    {
        /* ÊäÈë²ÎÊýÎª115200£¬×ª»»ÎªB115200,termiosœá¹¹ÌåÖÐÊ¹ÓÃB115200*/
        if (speed == name_arr[i])
        {
            tcflush(fd, TCIOFLUSH);  //Ë¢ÇåÊäÈë¡¢Êä³ö¶ÓÁÐ
            //cfsetispeed(&Opt, speed_arr[i]);//ÉèÖÃÊäÈë²šÌØÂÊ
            cfsetospeed(&Opt, speed_arr[i]);//ÉèÖÃÊä³ö²šÌØÂÊ
            status = tcsetattr(fd, TCSANOW, &Opt);//žüžÄÉèÖÃÁ¢ŒŽÉúÐ§

            if (status != 0)
            {
                perror("tcsetattr fd1 error");
                return;
            }
            else
            {
                printf("set fd1 ok \n");
            }

            tcflush(fd,TCIOFLUSH); //Ë¢ÇåÊäÈë¡¢Êä³ö¶ÓÁÐ
            }
    }
}

int main()
{
    //fdÓÃÀŽ±£ŽæÎÄŒþÃèÊö·û£¬
    int fd,flag,rd_num=0;
    struct termios term;//¶šÒåÒ»œá¹¹Ìå
    speed_t baud_rate_i,baud_rate_o,baud_rate_a,baud_rate_b;    //¶šÒå²šÌØÂÊ
    char recv_buf[20];//¶ÁÐŽÊ¹ÓÃµÄÊý×é£¬·¢ËÍ£¬œÓÊÕÁœÖÖÊý×é
    //fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK|O_NOCTTY | O_NDELAY);     //Žò¿ªÉè±žÎÄŒþ£¬Ê¹ÓÃUSB×ªŽ®¿Ú£¬Éè±žÎÄŒþÎª/dev/ttyUSB0 O_NOCTTY | O_NDELAY
    fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK);
    if(fd==-1)    //error
        printf("can not open the ttyUSB0!\n");
    else    //ok
        printf("open USB-Serial ttyUSB0 ok!\n");

    flag=tcgetattr(fd,&term);
    baud_rate_i=cfgetispeed(&term);
    baud_rate_o=cfgetospeed(&term);
    printf("baudrate of in is:%d,baudrate of out is%d,fd=%d\n",baud_rate_i,baud_rate_o,fd);/*ŽòÓ¡ÉèÖÃÖ®Ç°µÄ²šÌØÂÊ£¬Ä¿µÄÊÇ·œ±ãºÍÉèÖÃÖ®ºóµÄ²šÌØÂÊ¶Ô±È*/

    set_speed(fd,9600);/*ÖØÐÂÉèÖÃ²šÌØÂÊ*/
    /* tcgetattr Óë tcgetattr³É¹ŠÊ±·µ»Ø0  */
    flag=tcgetattr(fd,&term);/*ÒÔÏÂÈýÐÐ¶ÁÈ¡ÉèÖÃÖ®ºóµÄ²šÌØÂÊ£¬ÓÃcfgetispeedºÍcfgetospeedµÃµœµÄ²šÌØÂÊÊÇÒ»žöÐòºÅ£¬¿ÉÒÔÍš¹ý²é±í£š±íŒû³ÌÐòºóÃæ£©µÃµœÕæÕýµÄ²šÌØÂÊ£¬±ÈÈç·µ»Ø13£¬¶ÔÓŠµÄÊµŒÊ²šÌØÂÊÊÇ9600¡£ÎÒÕâÀïÃ»ÓÐ×ö×ª»»£¬Ö±œÓ°Ñ13Êä³öÁË¡£*/
    baud_rate_a=cfgetispeed(&term);/*ÉèÖÃÊäÈë²šÌØÂÊ*/
    baud_rate_b=cfgetospeed(&term);/*ÉèÖÃÊä³ö²šÌØÂÊ*/
    printf("baudrate of in is:%d,baudrate of out is%d,fd=%d,flag=%d\n,",baud_rate_a,baud_rate_b,fd,flag);/*ŽòÓ¡ÉèÖÃÖ®ºóµÄ²šÌØÂÊ£¬Ä¿µÄÊÇ·œ±ãºÍÉèÖÃÖ®ºóµÄ²šÌØÂÊ¶Ô±È*/

//    while(1)
//    {
//        read(fd,recv_buf,1);
//        if(recv_buf[0] == 0x55)
//        {
//            printf("Get data\n");
//            read(fd,recv_buf,10);
//            break;
//        }
//        printf("cur %x\n", recv_buf[0]);
//    }

    while(1)
    {
        rd_num=read(fd,recv_buf,11);/*ÔÙ¶Á³ö*//*·µ»ØÖµÊÇÕæÕý¶Á³öÁË¶àÉÙžö×Ö·û*/

//        printf("%x_%x_%d\n", recv_buf[0], recv_buf[1], rd_num);
        if(rd_num>0)
        {
            int vale = recv_buf[1];
//            printf("value %d,%x\n",vale,vale);
            if(vale == 81)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2] & 0xff);
				stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4] & 0xff);
				stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6] & 0xff);
				//stcAngle.T = ((unsigned short)recv_buf[9]<<8)|recv_buf[8];
//                printf("we can read \"%x_%x_%d_%d\" from the ttyUSB0.total:%d characters\n",recv_buf[0],recv_buf[1],recv_buf[2],recv_buf[3],rd_num);
//                printf("we can read \"%d_%d_%d_%d\" from the ttyUSB0.total:%d characters\n",recv_buf[4],recv_buf[5],recv_buf[6],recv_buf[7],rd_num);
                unsigned short num = '0x0';
                unsigned short nCheck = '0x0';

                num = (recv_buf[0] + recv_buf[1] + recv_buf[2] + recv_buf[3] + recv_buf[4] + recv_buf[5] +
                recv_buf[6] + recv_buf[7] + recv_buf[8] + recv_buf[9]) &255;
                nCheck = recv_buf[10]&255;
                if(num == nCheck)
                {
                    printf("Angle:%.4f %.4f %.4f\r\n",(float)stcAngle.Angle[0]/32768*16,(float)stcAngle.Angle[1]/32768*16,(float)stcAngle.Angle[2]/32768*16);
                }
                else
                {
                    continue;
                }
            }
        }
        else
        {
            //
        }
//            printf("read ttyUSB0 fail!\n");
        usleep(21500); //1000us = 1ms //²»Í¬µÄÊ±ŒäŒäžôµŒÖÂÊä³öÎÈ¶šÐÔ²»Í¬¡£21500 ×îºÃ¡£15000 ³öÏÖÆäËû²»×ŒÈ·ÊýŸÝžÅÂÊ1/3
    }
}

