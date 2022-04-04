#include <unistd.h>
#include <stdarg.h>
#define hex "0123456789abcdef"

static int	ft_putchar(char c)
{
	return (write(1, &c, 1));
}

static int	ft_putstr(char *s)
{
	int	ret = 0;
	if (!s)
		return (write(1, "(null)", 6));
	while (*s)
		ret += ft_putchar(*s++);
	return (ret);
}

static int ft_putnbr(long long n, int base)
{
    int ret = 0;

    if (n < 0)
    {
        ret += write(1, "-", 1);
        n *= -1;
    }
    if (n >= base)
        ret += ft_putnbr(n/base, base);
    ret += ft_putchar(hex[n%base]);
    return ret;
}

static int	print(const char *f, va_list ap)
{
	int ret = 0;
	char c;
	
	while (*f)
	{
		c = *f++;
		if (c != '%')
		{
			ret += ft_putchar(c);
		}
		else
		{
			c = *f++;
			if (c == 'c')
				ret += ft_putchar((char)va_arg(ap, int));
			else if (c == 's')
				ret += ft_putstr(va_arg(ap, char *));
			else if (c == 'd')
				ret += ft_putnbr((long long)va_arg(ap, int), 10);
			else if (c == 'x')
				ret += ft_putnbr((long long)va_arg(ap, unsigned int), 16);
		}
	}
	return (ret);
}

int	ft_printf(const char *f, ...)
{
	va_list ap;
	int	ret = 0;

	va_start(ap, f);
	ret += print(f, ap);
	va_end(ap);
	return (ret);
}