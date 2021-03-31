
build:
	python3 setup.py bdist_wheel

install:
	python3 -m pip install .

clean:
	python3 setup.py clean --all

