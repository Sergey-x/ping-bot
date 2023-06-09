format:
	isort .

test:
	pytest . -n 4

test-cov:
	pytest . --verbosity=2 --showlocals --log-level=DEBUG --cov=.

test-cov-save:
	pytest . --verbosity=2 --showlocals --log-level=DEBUG --cov=. --cov-report xml:cov.xml

check:
	isort . --check && \
	flake8 .

env:
	cp .env.example .env
