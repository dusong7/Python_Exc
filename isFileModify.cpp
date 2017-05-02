#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>

using namespace std;


bool  isMidify()
{

    return false;
}

bool fileWrite(bool bl)
{
    char *string1;
    if (bl)
    {
//        string1 = "1";
        memset(string1,0,0);
    }
    else
    {
//        string1 = "0";
        memset(string1,0,1);
    }
    FILE *file;
    file = fopen("file","w");
    fwrite(string1,1,1,file);
    fclose(file);
}
