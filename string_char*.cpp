string 与char* char[]之间的转换，有需要的朋友可以参考下。

1、首先必须了解，string可以被看成是以字符为元素的一种容器。字符构成序列（字符串）。有时候在字符序列中进行遍历，标准的string类提供了STL容器接口。具有一些成员函数比如begin()、end()，迭代器可以根据他们进行定位。

注意，与char*不同的是，string不一定以NULL('\0')结束。string长度可以根据length()得到，string可以根据下标访问。所以，不能将string直接赋值给char*。
2、string 转换成 char *

如果要将string直接转换成const char *类型。string有2个函数可以运用。

一个是.c_str()，一个是data成员函数。

例子如下：

string s1 = "abcdeg";

const char *k = s1.c_str();
const char *t = s1.data();

printf("%s%s",k,t);
cout<<k<<t<<endl;

如上，都可以输出。内容是一样的。但是只能转换成const char*，如果去掉const编译不能通过。

那么，如果要转换成char*，可以用string的一个成员函数copy实现。

string s1 = "abcdefg";

char *data;
int len = s1.length();

data = (char *)malloc((len+1)*sizeof(char));
s1.copy(data,len,0);

printf("%s",data);
cout<<data;

3、char *转换成string

可以直接赋值。

string s;

char *p = "adghrtyh";

s = p;

不过这个是会出现问题的。

有一种情况我要说明一下。当我们定义了一个string类型之后，用printf("%s",s1);输出是会出问题的。这是因为“%s”要求后面的对象的首地址。但是string不是这样的一个类型。所以肯定出错。

用cout输出是没有问题的，若一定要printf输出。那么可以这样：

printf("%s",s1.c_str())

4、char[] 转换成string
这个也可以直接赋值。但是也会出现上面的问题。需要同样的处理。

5、string转换成char[]
这个由于我们知道string的长度，可以根据length()函数得到，又可以根据下标直接访问，所以用一个循环就可以赋值了。

这样的转换不可直接赋值。

string pp = "dagah";

char p[8];
int i;

for( i=0;i<pp.length();i++)
p[i] = pp[i];

p[i] = '\0';
printf("%s\n",p);

cout<<p;


//
 system("ps -a | grep ProcessCmu1 >psOut");
    in.open("psOut");
    string string1;
    getline(in,string1);
    in.close();

    //cout<<string1<<endl;
    int i = string1.find('p');
//    string string2;
//    string2 = string1.substr(0,i-3);
//    int j = string2.find(' ');
//    string2 = string2.substr(j);
//    trim(string2);
//    cout<<string2<<endl;
    string1 = string1.substr(1,i-1);
    cout<<string1;
    string1
