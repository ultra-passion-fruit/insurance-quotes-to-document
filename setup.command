#!/bin/sh

# $0 gets the currently running shell script's path
# dirname returns only the path of a given [file], $0 in this case
# cd changes CWD into [path]
# needed since when double clicking file automatically runs in /usr/home directory

cd "$(dirname "$0")"

echo "Running path:"
pwd

echo "Creating Environment..."
python3.12 -m venv .venv

echo "Environment created."

echo "Installating dependencies via pip..."
source .venv/bin/activate
pip install -r req.txt

echo "Dependencies installed."

echo "Setup finished. You can close this window."
