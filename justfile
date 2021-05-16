build:
	python build.py
	
watch:
	ls templates/* build.py | entr  just build
	
setup-python:
	#!/bin/bash
	python3.8 -m venv env --without-pip
	source env/bin/activate
	curl https://bootstrap.pypa.io/get-pip.py | python
	pip install -r requirements.txt
	
	
