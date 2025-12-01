#! /usr/bin/env zsh

# Find the highest numbered folder
highest=$(ls -d [0-9][0-9] 2>/dev/null | sort -n | tail -n 1)

# Determine the next folder number
if [[ -z "$highest" ]]; then
    next="01"
else
    next=$(printf "%02d" $((10#$highest + 1)))
fi

# Create the next folder
mkdir "$next"

cp -R template/* "$next"

cd "$next"
# uv venv -p python3.12
uv venv -p python3.14
source .venv/bin/activate
uv pip install -r requirements.txt