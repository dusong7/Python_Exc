// Consol_.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;


int number(int N, int array[10])
{
	//
	int ncount[10] = {0};
	
	for (int i = 0; i < N; i++)
	{
		for (size_t j = 0; j < N; j++)
		{
			if (array[i] == j)
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
	cin >> N;

	for (size_t i = 0; i < N; i++)
	{
		cin >> array[i];
	}

	printf("%d\n", number(N, array));
	return 0;
}
