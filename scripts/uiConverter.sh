#!/bin/sh
for f in ui/*.ui; do
    filename=$(basename -- "$f")
    name="${filename%.*}"
    python3 -m PyQt5.uic.pyuic -x "ui/$name.ui" -o "src/generated/$name.py"
done
echo "Yippie"
