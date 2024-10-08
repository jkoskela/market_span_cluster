#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = market-span-cluster
PYTHON_VERSION = 3.11
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	
## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	black --check --config pyproject.toml market_span_cluster
	black --check --config pyproject.toml notebooks

## Format source code with black
.PHONY: format
format:
	black --config pyproject.toml market_span_cluster
	black --config pyproject.toml notebooks
