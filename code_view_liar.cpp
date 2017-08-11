// #include <iostream>
// using namespace std;


// int number(int N, int *array)
// {
// 	//
// 	int ncount[10] = {0};
	
// 	for (int i = 0; i < N; i++)
// 	{
// 		for (size_t j = 0; j < N; j++)
// 		{
// 			if (*array++ == j)
// 			{
// 				ncount[j]++;
// 			}
// 		}
// 	}

// 	for (size_t i = 0; i <= N; i++)
// 	{
// 		if (ncount[i] + i == N)
// 		{
// 			return i;
// 			break;
// 		}
// 	}

// 	return -1;
// }

// int main(void)
// {
// 	int array[10] = { 0 };
// 	int N;
// 	int *array1;
// 	cin >> N;
// 	array1 = (int *)malloc(N * sizeof(int));
// 	for (size_t i = 0; i < N; i++)
// 	{
// 		cin >> *array1++;
// 	}

// 	printf("%d\n", number(N, array1));
// 	return 0;
// }


/**
//说谎者问题
//通过计算求出 说谎者数 + 未说谎者数 = 总数
//Create By Du Songchang
//mail: dusong7@hotmail.com
//IDE: Code::Blocks
//compiler: gcc 4.9.2
**/

#include <stdio.h>
#include <stdlib.h>

int liarCount(int N, int *array)
{
    int nCount[10] = {0};
	//
    //统计出每组说谎者数量
    //e.g (0,1) 有0个说谎者的有1个人
    //算法复杂度为 O(n2)
    //STL 下可以用map来解决， 复杂度 O(logN)
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (*array++ == j)
			{
				nCount[j]++;
			}
		}
	}

	//计算出当列说谎者的数量+未说谎者的数量 = N的最小值
	//e.g (1,1),  1+1 == N ?
	//
	//
	for (int i = 0; i <= N; i++)
	{
		if (nCount[i] + i == N)
		{
			return i;
			break;
		}
	}

	return -1;
}

int main(void)
{
	int N;  //总人数
	int *arrayOri; //说谎者数据
	scanf("%d", &N);
    //N 值输入可能为负值
    //malloc 可能失败
    //
    if(N>0)
    {
        if( arrayOri = (int *)malloc(N * sizeof(int)))
        {
            for (size_t i = 0; i < N; i++)
            {
                scanf("%d", &*arrayOri++);
            }

            //
            printf("%d\n", liarCount(N, arrayOri));
            free(arrayOri);
        }
    }
	else
    {
        //
    }

	return 0;
}

