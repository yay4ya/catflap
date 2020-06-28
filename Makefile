PWD=$(shell pwd)
PYTHON=poetry run python
PYTEST=poetry run pytest
MYPY=poetry run mypy
PYLINT=poetry run pylint
PYLINTRC=$(PWD)/.pylintrc
MODULE=catflap

.PHONEY: test clean clean-pyc clean-build

test:
	PYTHONPATH=$(PWD) $(PYTEST)

mypy:
	PYTHONPATH=$(PWD) $(MYPY) $(MODULE)

lint:
	$(PYLINT) --rcfile=$(PYLINTRC) $(MODULE)

clean: clean-pyc clean-build

clean-pyc:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf $(MODULE).egg-info/
	rm -rf pip-wheel-metadata/
