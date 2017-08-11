#include <iostream>
using namespace std;


int number(int N, int *array)
{
	//
	int ncount[10] = {0};
	
	for (int i = 0; i < N; i++)
	{
		for (size_t j = 0; j < N; j++)
		{
			if (*array++ == j)
			{
				ncount[j]++;
			}
		}
	}

	for (size_t i = 0; i <= N; i++)
	{
		if (ncount[i] + i == N)
		{
			return i;
			break;
		}
	}

	return -1;
}

int main(void)
{
	int array[10] = { 0 };
	int N;
	int *array1;
	cin >> N;
	array1 = (int *)malloc(N * sizeof(int));
	for (size_t i = 0; i < N; i++)
	{
		cin >> *array1++;
	}

	printf("%d\n", number(N, array1));
	return 0;
}
