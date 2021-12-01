#!/usr/bin/python

import os
import sys

if(len(sys.argv) != 4):
  print("Usage: rename.py DIRECTORY OLD-EXTENSION NEW-EXTENSION")
  sys.exit(1)

dir = sys.argv[1]
old = sys.argv[2]
new = sys.argv[3]

def rename_ext(root):
  root = os.path.abspath(root)
  for entry in os.listdir(root):
    fullname = os.path.join(root, entry)
    if os.path.isfile(fullname):
      filename, ext = os.path.splitext(fullname)
      if ext == "." + old:
        os.rename(fullname, filename + "." + new)
    if os.path.isdir(fullname):
      rename_ext(fullname)

rename_ext(dir)
