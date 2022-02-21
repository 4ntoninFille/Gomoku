##
## EPITECH PROJECT, 2021
## Mini-Pacman
## File description:
## Makefile
##

NAME 	= 	pbrain-gomoku-ai

all: $(NAME)

$(NAME):
	cp src/main.py $(NAME)
	chmod +x $(NAME)

buildpy: fclean
	pyinstaller --onefile src/main.py --name $(NAME)
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
