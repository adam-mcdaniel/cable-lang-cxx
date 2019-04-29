cd ~
git clone https://github.com/adam-mcdaniel/cable-lang-cxx
cd cable-lang-cxx
make build
cp -R bin/* release/unix
make unix
cd ..
rm -Rf cable-lang-cxx