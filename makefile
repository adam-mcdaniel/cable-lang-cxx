build:
	rm -Rf bin
	mkdir bin
	cd cable; make install
	cd wire; make install; mv ./wire ../bin/wire; cp -Rf ./project ../bin/project

unix:
	rm -Rf ~/cablelang | true
	mkdir ~/cablelang | true
	cp -Rf release/unix ~/cablelang/
	mv -f ~/cablelang/unix ~/cablelang/bin
	echo 'export PATH="$$HOME/cablelang/bin:$$PATH"' >> ~/.bashrc
	echo 'export PATH="$$HOME/cablelang/bin:$$PATH"' >> ~/.profile
	echo 'export PATH="$$HOME/cablelang/bin:$$PATH"' >> ~/.bash_profile