#include <stdio.h>
#include <string>

void executeCMD(const char *cmd, char *result)
{
    char buf_ps[1024];
    char ps[1024]={0};
    FILE *ptr;
    strcpy(ps, cmd);
    if((ptr=popen(ps, "r"))!=NULL)
    {
        while(fgets(buf_ps, 1024, ptr)!=NULL)
        {
           strcat(result, buf_ps);
           if(strlen(result)>1024)
               break;
        }
        pclose(ptr);
        ptr = NULL;
    }
    else
    {
        printf("popen %s error\n", ps);
    }
}

int main()
{
        char result[1024];
        executeCMD( "ls /opt/*.rpm | awk -F '[-|.]' '{print $3}'", result);
        printf("%s", result );
        return 0;
}
