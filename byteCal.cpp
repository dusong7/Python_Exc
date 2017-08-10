#include <stdio.h>
#include <windows.h>

int main()
{
    int number = 100;
    int value = 1<<24 | 0<<16 | number;
    printf("%d\n", value);

    printf("%d_%d_%d", value>>24, value>>8 & 0xff, value & 0xffff);

    return 0;
}
