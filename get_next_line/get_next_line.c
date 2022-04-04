#include "get_next_line.h"

char *ft_strdup(char *str)
{
	char *res;
	int i = 0;
	int len = 0;

	while (str[len])
		len++;
	res = malloc(sizeof(char) * (len + 1));
	if (res == 0)
		return 0;
	while (i < len)
	{
		res[i] = str[i];
		i++;
	}
	res[i] = 0;
	return (res);
}

char *get_next_line(int fd)
{
	char arr[9999999] = {0};
	char buff;
	int i = 0;
	int nbyte = 0;

	if(fd < 0 || BUFFER_SIZE <= 0)
		return 0;
	while((nbyte = read(fd, &buff, 1)) && nbyte > 0)
	{
		arr[i++] = buff;
		if(buff == '\n')
			break;
	}
	arr[i] = 0;
	if(nbyte <= 0 && i == 0)
		return 0;
	return (ft_strdup(arr));
}
