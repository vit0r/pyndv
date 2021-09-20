tox: 
	rm -fr .tox .coverage 
	tox 
	find . -name '*.pyc' -delete 
	find . -name '__pycache__' -type d | xargs rm -fr	
	rm -fr *.egg *.egg-info/ dist/ build/ docs/_build/
lint:
	isort pyndv tests
	black pyndv tests
	flake8 pyndv tests
release: 
	rm -fr *.egg *.egg-info/ dist/ build/ docs/_build/
	python setup.py sdist
	twine check --strict dist/*
	twine upload --repository pyndv dist/*