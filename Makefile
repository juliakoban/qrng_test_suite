PYTHON = python3
TEST_DIR = unittests  

FILE ?= ./data/QNGFile.dat
BITS ?= 40000
BITSTREAMS ?= 100

all: run_default

run:
	$(PYTHON) main.py --file $(FILE) --bits $(BITS) --bitstreams $(BITSTREAMS)

run_default:
	$(PYTHON) main.py

help:
	$(PYTHON) main.py --help

test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)