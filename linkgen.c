#include <stdio.h>

void init(char *mat)
{
	int n = 0;
	for (char i = '0'; i <= '9'; ++i, ++n)
	{
		mat[n] = i;
	}
	{
		mat[n] = '_';
		++n;
		mat[n] = '-';
		++n;
	}
	for (char i = 'A'; i <= 'Z'; ++i, ++n)
	{
		mat[n] = i;
	}
	for (char i = 'a'; i <= 'z'; ++i, ++n)
	{
		mat[n] = i;
	}
}

int main(void)
{

}