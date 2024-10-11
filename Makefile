PYTHON = python3
TEST_DIR = unittests  

all: run

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)