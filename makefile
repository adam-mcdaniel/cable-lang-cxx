install:
	rm -Rf bin
	mkdir bin
	cd cable; make install
	cd wire; make install; mv ./wire ../bin/wire; cp -Rf ./project ../bin/project