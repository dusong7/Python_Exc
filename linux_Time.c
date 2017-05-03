
本文旨在为了解Linux各种时间类型与时间函数提供技术文档。

1、Linux下常用时间类型
Linux下常用时间类型有四种：time_t、struct tm、struct timeval、struct timespec

1.1 time_t时间类型
time_t类型在time.h中定义：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
#ifndef __TIME_T  
#define __TIME_T  
typedef  long  time_t;  
#endif  
可见，time_t实际是一个长整型。其值表示为从UTC(coordinated universal time)时间1970年1月1日00时00分00秒(也称为Linux系统的Epoch时间)到当前时刻的秒数。由于time_t类型长度的限制，它所表示的时间不能晚于2038年1月19日03时14分07秒(UTC)。为了能够表示更久远的时间，可用64位或更长的整形数来保存日历时间，这里不作详述。
使用time()函数获取当前时间的time_t值，使用ctime()函数将time_t转为当地时间字符串。
备注：UTC时间有时也称为GMT时间，其实UTC和GMT两者几乎是同一概念。它们都是指格林尼治标准时间，只不过UTC的称呼更为正式一点。两者区别在于前者是天文上的概念，而后者是基于一个原子钟。

1.2 struct tm时间类型
tm结构在time.h中定义：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
#ifndef _TM_DEFINED  
struct tm{  
    int tm_sec; /*秒 - 取值区间为[0, 59]*/  
    int tm_min; /*分 - 取值区间为[0, 59]*/  
    int tm_hour; /*时 - 取值区间为[0, 23]*/  
    int tm_mday; /*日 - 取值区间为[1, 31]*/  
    int tm_mon; /*月份 - 取值区间为[0, 11]*/  
    int tm_year; /*年份 - 其值为1900年至今年数*/  
    int tm_wday; /*星期 - 取值区间[0, 6]，0代表星期天，1代表星期1，以此类推*/  
    int tm_yday; /*从每年的1月1日开始的天数-取值区间为[0, 365]，0代表1月1日*/  
    int tm_isdst; /*夏令时标识符，使用夏令时，tm_isdst为正，不使用夏令时，tm_isdst为0，不了解情况时，tm_isdst为负*/  
};  
#define _TM_DEFINED  
#endif  
ANSI C标准称使用tm结构的这种时间表示为分解时间(broken-down time)。
使用gmtime( )和localtime( )可将time_t时间类型转换为tm结构体；
使用mktime( )将tm结构体转换为time_t时间类型；
使用asctime( )将struct tm转换为字符串形式。
 
1.3 struct timeval时间类型
timeval结构体在time.h中定义：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
Struct tmieval{  
    time_t tv_sec; /*秒s*/  
    suseconds_t tv_usec; /*微秒us*/  
};  
设置时间函数settimeofday( )与获取时间函数gettimeofday( )均使用该事件类型作为传参。
 
1.4 struct timespec时间类型
timespec结构体在time.h定义：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
struct timespec{  
    time_t tv_sec; /*秒s*/  
    long tv_nsec; /*纳秒ns*/  
};  
 
2、Linux下常用时间函数
Linux下常用时间函数有：time( )、ctime( )、gmtime( )、localtime( )、mktime( )、asctime( )、difftime( )、gettimeofday( )、settimeofday( )

2.1 time( )函数
头文件：#include <time.h>
函数定义：time_t time(time_t *timer)
功能描述：该函数返回从1970年1月1日00时00分00秒至今所经过的秒数。如果time_t *timer非空指针，函数也会将返回值存到timer指针指向的内存。
返回值：成功则返回秒数，失败则返回((time_t)-1)值，错误原因存于errno中。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
time_t seconds;  
seconds = time((time_t *)NULL);  

2.2 ctime( )函数
头文件：#include <time.h>
函数定义：char *ctime(const time_t *timep);
功能描述：ctime( )将参数timep指向的time_t时间信息转换成实际所使用的时间日期表示方法，并以字符串形式返回。字符串格式为："Wed Jun 20 21:00:00 2012\n"。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
time_t timep;  
tmep = time(NULL);  
printf("%s\n", ctime(&timep));  

2.3 gmtime( )函数
头文件：#include <time.h>
函数定义：struct tm *gmtime(const time_t *timep)
功能描述：gmtime( )将参数timep指向的time_t时间信息转换成以tm结构体表示的GMT时间信息，并以struct tm*指针返回。
GMT：GMT是中央时区,北京在东8区,相差8个小时，所以北京时间=GMT时间+8小时。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    char *wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};  
    time_t timep;  
    struct tm *p_tm;  
    timep = time(NULL);  
    p_tm = gmtime(&timep); /*获取GMT时间*/  
    printf("%d-%d-%d ", (p_tm->tm_year+1900), (p_tm->mon+1), p_tm->tm_mday);  
    printf("%s %d:%d:%d\n", wday[p_tm->tm_wday], p_tm->tm_hour, p_tm->tm_min, p_tm->tm_sec);  
}  

2.4 localtime( )函数
头文件：#include <time.h>
函数定义：struct tm *localtime(const time_t *timep);
功能描述：localtime( )将参数timep指向的time_t时间信息转换成以tm结构体表示的本地时区时间(如北京时间= GMT+小时)。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    char *wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};  
    time_t timep;  
    struct tm *p_tm;  
    timep = time(NULL);  
    p_tm = localtime(&timep); /*获取本地时区时间*/  
    printf("%d-%d-%d ", (p_tm->tm_year+1900), (p_tm->mon+1), p_tm->tm_mday);  
    printf("%s %d:%d:%d\n", wday[p_tm->tm_wday], p_tm->tm_hour, p_tm->tm_min, p_tm->tm_sec);  
    return 0;  
}  

2.5 mktime( )函数
头文件：#include <time.h>
函数定义：time_t mktime(struct tm *p_tm);
功能描述：mktime( )将参数p_tm指向的tm结构体数据转换成从1970年1月1日00时00分00秒至今的GMT时间经过的秒数。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    time_t timep:  
    struct tm *p_tm;  
    timep = time(NULL);  
    pintf("time( ):%d\n", timep);  
    p_tm = local(&timep);  
    timep = mktime(p_tm);  
    printf("time( )->localtime( )->mktime( ):%d\n", timep);  
    return 0;  
}  

2.6 asctime( )函数
头文件：#include <time.h>
函数定义：char *asctime(const struct tm *p_tm);
功能描述：asctime( )将参数p_tm指向的tm结构体数据转换成实际使用的时间日期表示方法，并以字符串形式返回(与ctime函数相同)。字符串格式为："Wed Jun 20 21:00:00 2012\n"。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    time_t timep;  
    timep = time(NULL);  
    printf("%s\n", asctime(gmtime(&timep)));  
    return 0;  
}  

2.7 difftime( )函数
头文件：#include <time.h>
函数定义：double difftime(time_t timep1, time_t timep2);
功能描述：difftime( )比较参数timep1和timep2时间是否相同，并返回之间相差秒数。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    time_t timep1, timep2;  
    timep1 = time(NULL);  
    sleep(2);  
    timep2 = time(NULL);  
    printf("the difference is %f seconds\n", difftime(timep1, timep2));  
    return 0;  
}  

2.8 gettimeofday( )函数
头文件：#include <sys/time.h>
        #include <unistd.h>
函数定义：int gettimeofday(struct timeval *tv, struct timezone *tz);
功能描述：gettimeofday( )把目前的时间信息存入tv指向的结构体，当地时区信息则放到tz指向的结构体。
struct timezone原型：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
struct timezone{  
    int tz_minuteswest; /*miniutes west of Greenwich*/  
    int tz_dsttime; /*type of DST correction*/  
};  
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
struct timeval tv;  
struct timeval tz;  
gettimeofday(&tv, &tz);  

附：
使用time函数族获取时间并输出指定格式字符串例子（strftime( )函数）：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    char strtime[20] = {0};  
    time_t timep;  
    struct tm *p_tm;  
    timep = time(NULL);  
    p_tm = localtime(&timep);  
    strftime(strtime, sizeof(strtime), "%Y-%m-%d %H:%M:%S", p_tm);  
    return 0;  
}  

2.9 settimeofday( )函数
头文件：#include <sys/time.h>
        #include <unistd.h>
函数定义：int settimeofday(const struct timeval *tv, const struct timezone *gz);
功能描述：settimeofday( )把当前时间设成由tv指向的结构体数据。当前地区信息则设成tz指向的结构体数据。
例：
[cpp] view plain copy print?在CODE上查看代码片派生到我的代码片
int main(void)  
{  
    char t_string[] = "2012-04-28 22:30:00";  
    struct tm time_tm;  
    struct timeval time_tv;  
    time_t timep;  
    int ret = 0;  
  
    sscanf(t_string, "%d-%d-%d %d:%d:%d", &time_tm.tm_year, &time_tm.tm_mon, &time_tm.tm_mday, &time_tm.tm_hour, &time_tm.tm_min, &time_tm.tm_sec);  
    time_tm.tm_year -= 1900;  
    time_tm.tm_mon -= 1;  
    time_tm.tm_wday = 0;  
    time_tm.tm_yday = 0;  
    time_tm.tm_isdst = 0;  
  
    timep = mktime(&time_tm);  
    time_tv.tv_sec = timep;  
    time_tv.tv_usec = 0;  
  
    ret = settimeofday(&time_tv, NULL);  
    if(ret != 0)  
    {  
        fprintf(stderr, "settimeofday failed\n");  
        return -1;  
    }  
    return 0;  
}  

参考资料：
http://blog.csdn.net/c395565746c/article/details/6621153
http://fanqiang.chinaunix.net/a4/b8/20010527/201001267.html
http://qgjie456.blog.163.com/blog/static/35451367200844102949365/
http://hi.baidu.com/wangzhongli/blog/item/e260b3a1f388278746106461.html
http://www.eefocus.com/xuefu2009/blog/10-03/187348_f456a.html
http://www.instructables.com/id/EMLW5UGI26MZLAY/2014-11-08
