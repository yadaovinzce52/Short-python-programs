#!/usr/bin/python

import sys
import os

def isVowel(l):
  if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    return True
  else:
    return False

if os.path.isfile(sys.argv[1]):
  size = len(open(sys.argv[1]).readlines())
  with open(sys.argv[1], 'r') as f:
    contents = [line.rstrip() for line in f]
else:
  print ("file does not exist")

vow1 = ''
vow2 = ''

for i in range(size-1):
  for j in range(0, size-i-1):
    str1 = contents[j]
    str2 = contents[j+1]
    for letter in str1:
      if isVowel(letter):
        vow1 += letter
      else:
        continue
    for letter in str2:
      if isVowel(letter):
        vow2 += letter
      else:
        continue
    if vow1 > vow2:
      contents[j], contents[j+1] = contents[j+1], contents[j]
      vow1 = ''
      vow2 = ''
for words in contents:
  print(words)
        
