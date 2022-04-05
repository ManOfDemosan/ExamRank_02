#include <unistd.h>
#include <stdarg.h>
#define hex "0123456789abcdef"

int	putchar(char c)
{
	return(write(1, &c, 1));
}

int putstr(char *str)
{
	int res = 0;

	if(!str)
		return(write(1, "(null)", 6));
	while(*str)
		res += putchar(*str++);
	return res;
}

int putnbr(long long n, int base) 
{
	int res = 0;

	if(n < 0)
	{
		res += write(1, "-",1);
		n *= -1;
	}
	if(n >= base)
		res += putnbr(n/base, base);
	res += putchar(hex[n%base]);
	return res;
}

int print(va_list ap, const char *str)
{
	int res = 0;
	char c;

	while (*str)
	{
		c = *str++;
		if(c != '%')
			res += putchar(c);
		else
		{
			c = *str++;
			if(c == 's')
				res += putstr(va_arg(ap, char *));
			else if(c == 'd')
				res += putnbr((long long) va_arg(ap, int), 10);
			else if(c == 'x')
				res += putnbr((long long) va_arg(ap, unsigned int), 16);
		}
	}
	return res;
}

int ft_printf(const char *str, ...)
{
	va_list ap;
	int res = 0;

	va_start(ap, str);
	res += print(ap, str);
	va_end(ap);
	return(res);
}
