#Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI

lint:
	poetry run flake8 brain_games
