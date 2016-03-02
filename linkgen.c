#include <stdio.h>

void init(int *mat)
{
	int n = 0;
	for (int i = '0'; i <= '9'; ++i, ++n)
	{
		mat[n] = i;
	}
	{
		mat[n] = '_';
		++n;
		mat[n] = '-';
		++n;
	}
	for (int i = 'A'; i <= 'Z'; ++i, ++n)
	{
		mat[n] = i;
	}
	for (int i = 'a'; i <= 'z'; ++i, ++n)
	{
		mat[n] = i;
	}
}

void input_data(int *basic)
{
	int sym;
	int cnt = 0;
	int state = 0;
	while ((sym = getchar()) != EOF && cnt < 57) {
		if (cnt < 39) {
			cnt++;
			continue;
		}
		if (sym == '/') {
			state++;
			continue;
		}
	}
}

int main(void)
{
	int element1[2];
	int element2[11];
	int element3;

}