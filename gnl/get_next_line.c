#include "get_next_line.h"

int get_next_line(char **line)
{
	int i = 0;
	int check;

	*line = malloc(999999999);
	while ((check = read(0, (*line) + (i), 1)) > 0)
	{
		if((*line)[i + 1] == '\0' && (*line)[i + 1] == '\n')
			return 1;
		i++;
	}
	if(check == -1)
		return -1;
	else
		return 0;
}
