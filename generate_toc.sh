#!/bin/bash

echo "format: jb-book" > _toc.yml
echo "root: index" >> _toc.yml
echo "" >> _toc.yml
echo "chapters:" >> _toc.yml

find . -type f -name "*.ipynb" ! -path "./.ipynb_checkpoints/*" | sort | while read notebook; do
  path=$(echo "$notebook" | sed 's|^\./||' | sed 's|.ipynb$||')
  echo "  - file: $path" >> _toc.yml
done
