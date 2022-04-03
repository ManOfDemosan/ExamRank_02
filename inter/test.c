#include <unistd.h>

int	check(char *str, char c, int index)
{
	int i = 0;

	while(i < index)
	{
		if(str[i] == c)
			return 1;
		i++;
	}
	return 0;
}
int	main(int ac,char **av)
{
	int i;
	int j;

	if(ac == 3)
	{
		i = 0;
		while(av[1][i] != 0)
		{
			if (check(av[1],av[1][i],i) == 0)
			{
				j = 0;
				while(av[2][j] != 0)
				{
					if (av[1][i] == av[2][j])
					{
						write(1, &av[1][i], 1);
						break;
					}
					j++;
				}
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return 0;
}
