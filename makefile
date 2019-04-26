build:
	rm -Rf bin
	mkdir bin
	cd cable; make install
	cd wire; make install; mv ./wire ../bin/wire; cp -Rf ./project ../bin/project
	./update.sh

mac:
	rm -Rf ~/cablelang | true
	mkdir ~/cablelang | true
	cp -Rf release/mac ~/cablelang/
	mv -f ~/cablelang/mac ~/cablelang/bin
	echo 'export PATH="$$HOME/cablelang/bin:$$PATH"' >> ~/.profile
	echo 'export PATH="$$HOME/cablelang/bin:$$PATH"' >> ~/.bash_profile