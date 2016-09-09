.PHONY: help clean clean-pyc clean-build docs docs-fresh

help:
	@echo "clean - remove build artifacts"
	@echo "sdist - package"
	@echo "test-release - package and upload a release to the test PyPI server"
	@echo "release - package and upload a release"

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

sdist: clean
	python setup.py sdist
	ls -l dist
	check-manifest
	pyroma dist/`ls -t dist | head -n1`

test-release: sdist
	python setup.py register -r https://testpypi.python.org/pypi
	python setup.py sdist bdist_wheel upload -r https://testpypi.python.org/pypi
	python -m webbrowser -n https://testpypi.python.org/pypi/mdn-sphinx-theme

release: sdist
	python setup.py sdist bdist_wheel upload
	python -m webbrowser -n https://pypi.python.org/pypi/mdn-sphinx-theme
