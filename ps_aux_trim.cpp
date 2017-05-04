#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include  <stdio.h>
#include  <stdlib.h>
#include <zconf.h>
#include <stdlib.h>


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
        if (access("file",0) != -1)
        {
            remove("file");
        }
    }
    else
    {
//        string1 = "0";
        //memset(string1,0,1);
        file = fopen("1","w");
        //fwrite("0",2,2,file);
        remove("file");
    }
//    FILE *file;
//    file = fopen("file","w");
//    fwrite(string1,1,1,file);
    fclose(file);
}

void trim(string &s)
{

    if( !s.empty() )
    {
        s.erase(0,s.find_first_not_of(" "));
        s.erase(s.find_last_not_of(" ") + 1);
    }

}

int main()
{
    //
   // fileWrite(false);
//    char *str1;
//    char* str = gets(str1);
//    printf("%s", str);
//    string string2;
//    system("ps -aux | grep 'xterm -T ProcessCmu1' > file");
//    ifstream infile;
//    infile.open("file");
////    char *string1;
//
//    while(getline(string2,infile))
//    {
//        std::cout<<string2;
//    }
//    ofstream out;
    ifstream in;

//    out.open("psOut");
//    out<<"Hello";
//    out.close();
    system("ps -aux | grep ProcessCmu1 >psOut");
    in.open("psOut");
    string string1;
    getline(in,string1);
    //cout<<string1<<endl;
    int i = string1.find('.');
    string string2;
    string2 = string1.substr(0,i-3);
    int j = string2.find(' ');
    string2 = string2.substr(j);
    trim(string2);
    cout<<string2<<endl;
    //cout<<j;
//    const string command = "kill "+string2;
//    system(command);

    return 0;
}
