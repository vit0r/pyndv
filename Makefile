run-bumpversion: 
	bumpversion release --allow-dirty --new-version=$(buildnumber)
run-tox: 
	rm -fr .tox .coverage 
	tox 
	find . -name '*.pyc' -delete 
	find . -name '__pycache__' -type d | xargs rm -fr	
	rm -fr *.egg *.egg-info/ dist/ build/ docs/_build/
run-lint:
	isort pyndv tests
	black pyndv tests
	flake8 pyndv tests