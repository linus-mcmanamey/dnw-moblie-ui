git_setup:
	git config --global credential.helper store
	git config --global credential.interactive auto
	git config --global credential.useHttpPath true
	git config --global user.email linus.mcmanamey@gmail.com
	git config --global user.name linus-mcmanamey
	git config --global --add safe.directory ~/development/dnw-moblie-ui

install_python:
	sudo apt install python3-pip
	sudo apt-get install python3-venv

install_requirements:
	python3 -m venv .venv
	pip install -r requirements.txt

venv:
	source .venv/bin/activate