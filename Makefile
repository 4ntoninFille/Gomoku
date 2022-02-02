##
## EPITECH PROJECT, 2021
## Mini-Pacman
## File description:
## Makefile
##

SRC			=	main.py

NAME 	= 	pbrain-gomoku-ai

all: $(NAME)

$(NAME):
	cp main.py $(NAME)
	chmod +x $(NAME)

buildpy: fclean
	pyinstaller --onefile main.py --name $(NAME)
	cp dist/$(NAME) ./

clean:
	rm -rf pbrain-gomoku-ai

fclean: clean
	rm -rf __pycache__
	rm -rf build/
	rm -rf dist/
	rm -f $(NAME).spec

re: fclean all

.PHONY: all clean fclean re