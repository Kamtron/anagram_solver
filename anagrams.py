from itertools import permutations, islice
import threading
import time
from math import factorial

def calcEvenPermutations(s,word_list):
  matches = set()
  n = factorial(len(s))
  for x in islice(permutations(s),0,n,2):
    p = ''.join(x)
    if(p in word_list and p != s):
      matches.add(p)
  return matches

def calcOddPermutations(s,word_list):
  matches = set()
  n = factorial(len(s))
  for x in islice(permutations(s),1,n,2):
    p = ''.join(x)
    if(p in word_list and p != s):
      matches.add(p)
  return matches
  

def findAnagramMatches(s,word_list):
  matches = calcEvenPermutations(s,word_list)
  matches2 = calcOddPermutations(s,word_list)
  return matches.union(matches2)

def loadWordList(filename):
    f = open(filename,"r")
    word_list = set()
    for line in f:
      word_list.add(line.rstrip())
    f.close()
    return word_list

if __name__ == "__main__":
  print("Loading word list")
  word_list = loadWordList("words.txt")
  print("Ready")
  while(1):
    s = raw_input("Enter a string (or q to quit): ")
    if s == "q":
      break
    begin = time.time()
    matches = findAnagramMatches(s,word_list)
    end = time.time()
    if(len(matches) > 0):
      print("Matches for "+s+": ")
      for m in matches:
        print(m)
    else:
      print("No matches for "+s)
    print("took " + str(end-begin) + " seconds")

