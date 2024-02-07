GIT_ROOT = $(shell git rev-parse --show-toplevel)
SRC_PATH = $(GIT_ROOT)/src

INTERPRETER = $(shell which python3)
PIP = $(shell which pip3)

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  help:  Show this help message"
	@echo "  setup: Install all dependencies"
	@echo "  run:   Run the application"

check_py:
	@if [ -z "$(INTERPRETER)" ]; then \
		echo "Python3 is not installed"; \
		exit 1; \
	fi

check_pip:
	@if [ -z "$(PIP)" ]; then \
		echo "Pip3 is not installed"; \
		exit 1; \
	fi

check_linter:
	@if [ -z "$(LINTER)" ]; then \
		echo "Pylint is not installed"; \
		exit 1; \
	fi

install_requirements: check_py
	@$(INTERPRETER) -m pip install -r requirements.txt

setup: check_py check_pip install_requirements
	@echo "Setup complete"

run:
	@$(INTERPRETER) $(SRC_PATH)/main.py

.PHONY: help setup run lint