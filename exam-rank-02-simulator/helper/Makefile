NAME 		= 	libftprintf.a
CFLAGS		= 	-Wall -Werror -Wextra -c
CC			= 	cc
RM			= 	rm -f
AR			= 	ar -rcs
FILES		= 	../rendu/ft_printf/ft_printf.c
OBJ			= 	$(FILES:.c=.o)

all: $(NAME)

$(NAME):
	@$(CC) $(CFLAGS) $(FILES)
	@mv ft_printf.o ../rendu/ft_printf/
	@$(AR) $(NAME) $(OBJ)

clean:
	@$(RM) $(OBJ)

fclean: clean
	@$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
