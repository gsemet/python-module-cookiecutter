all: dev test

dev:
	pipenv install --dev --skip-lock

test:
	./test.sh
