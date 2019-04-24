

build:
	clear
	# python3 compiler.py examples/main.cb
	python3 compiler.py examples/file.cb
	g++ test.cpp -std=c++17 -o o
	./o
