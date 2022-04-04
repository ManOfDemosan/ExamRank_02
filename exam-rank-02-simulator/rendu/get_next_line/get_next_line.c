#include "get_next_line.h"

char	*ft_strdup(char *str)
{
	char *ret;
	int len	= 0;
	while (str[len])
		len++;
	ret = malloc(sizeof(char) * (len + 1));
	if (!ret)
		return (NULL);
	int	i = -1;
	while (++i < len)
		ret[i] = str[i];
	ret[i] = 0;
	return (ret);
}

char	*get_next_line(int fd)
{
	char heap[9999999] = {0};
	char buff;
	int nbyte = 0;
	int i = 0;
	if (fd < 0 && BUFFER_SIZE <= 0)
		return (NULL);
	while ((nbyte = read(fd, &buff, 1)) && nbyte > 0)
	{
		heap[i++] = buff;
		if (buff == '\n')
			break ;
	}
	heap[i] = 0;
	if (nbyte <= 0 && i == 0)
		return (NULL);
	return (ft_strdup(heap));
}
