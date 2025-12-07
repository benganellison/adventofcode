#! /usr/bin/env bash

# Run all the python scripts the subdirectories of this directory
source .venv/bin/activate
for dir in $(ls -d [0-9][0-9]); do
    echo "Running scripts in $dir"
    cd $dir
    #source .venv/bin/activate
    for script in $(ls part*.py); do
        printf "\n\n"
        echo "Running $dir / $script"
        time python $script
        printf "\n----------------------"
    done
    printf "\------------------\n\n"
    cd ..
done