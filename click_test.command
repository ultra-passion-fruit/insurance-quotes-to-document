#!/bin/sh

# $0 gets the currently running shell script's path
# dirname returns only the path of a given [file], $0 in this case
# cd changes CWD into [path]
# needed since when double clicking file automatically runs in /usr/home directory

cd "$(dirname "$0")"

echo "Running path:"
pwd

# run python script
python contents/quotes_calculation.py
