uninstall: # run by make uninstall
	rm -rf venv/
	rm -rf src/demo_package.egg-info
	rm -rf src/demo_package/__pycache__

install: # run by make install
	python -m venv "venv"
	venv/bin/python -m pip install -r "requirements.txt" -e .

reinstall: uninstall install # run by make reinstall

compile: # make compile
	venv/bin/python -m pip freeze --exclude-editable > "requirements.txt"
