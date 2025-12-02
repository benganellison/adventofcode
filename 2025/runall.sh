#! /usr/bin/env bash

# Run all the python scripts the subdirectories of this directory

for dir in $(ls -d [0-9][0-9]); do
    echo "Running scripts in $dir"
    cd $dir
    source .venv/bin/activate
    for script in $(ls part*.py); do
        echo "Running $dir / $script"
        time python $script
    done
    cd ..
done