
#!/bin/bash

for foldername in examples/*; 
do
    ./bin/wire update $foldername;
done