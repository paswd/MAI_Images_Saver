#include <stdio.h>
#include <stdlib.h>

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
	char matrix[64];
	init(matrix);
	char output[58];
	scanf("%s", output);
	for(int i1 = 0; i1 < 64; ++i1)
	{
		output[39] = matrix[i1];
		for (int i2 = 0; i2 < 64; ++i2)
		{
			output[40] = matrix[i2];
			for (int i3 = 0; i3 < 64; ++i3)
			{
				output[42] = matrix[i3];
				for (int i4 = 0; i4 < 64; ++i4)
				{
					output[43] = matrix[i4];
					for (int i5 = 0; i5 < 64; ++i5)
					{
						output[44] = matrix[i5];
						for (int i6 = 0; i6 < 64; ++i6)
						{
							output[45] = matrix[i6];
							for (int i7 = 0; i7 < 64; ++i7)
							{
								output[46] = matrix[i7];
								for (int i8 = 0; i8 < 64; ++i8)
								{
									output[47] = matrix[i8];
									for (int i9 = 0; i9 < 64; ++i9)
									{
										output[48] = matrix[i9];
										for (int i10 = 0; i10 < 64; ++i10)
										{
											output[49] = matrix[i10];
											for (int i11 = 0; i11 < 64; ++i11)
											{
												output[50] = matrix[i11];
												for (int i12 = 0; i12 < 64; ++i12)
												{
													output[51] = matrix[i12];
													for (int i13 = 0; i13 < 64; i13 += 4)
													{
														output[52] = matrix[i13];
														puts(output);
										
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}