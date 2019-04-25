

install:
	rm project/cable; rm -Rf project/include
	cd ../cable; make install; cp cable ../wire/project/cable; cp -R include ../wire/project/include

	pyinstaller --onefile main.py --distpath . -n wire
	rm project/wire
	cp wire project/wire
	rm wire.spec
	rm -Rf build
	rm -Rf __pycache__