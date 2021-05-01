.PHONY: test
test:
	python -m unittest test

.PHONY: install
install:
	python app_install.py

.PHONY: uninstall
uninstall:
	python app_uninstall.py

.PHONY: run
run:
	uvicorn app.main:app --reload