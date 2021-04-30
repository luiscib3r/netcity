.PHONY: test
test:
	python -m unittest test

.PHONY: install
install:
	python app_install.py

.PHONY: uninstall
uninstall:
	python app_uninstall.py