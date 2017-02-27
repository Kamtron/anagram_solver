from itertools import permutations, islice
import threading
import time
from math import factorial

def calcEvenPermutations(s,word_list,matches):
  n = factorial(len(s))
  for x in islice(permutations(s),0,n,2):
    p = ''.join(x)
    if(p in word_list and p != s):
      matches.add(p)
  return

def calcOddPermutations(s,word_list,matches):
  n = factorial(len(s))
  for x in islice(permutations(s),1,n,2):
    p = ''.join(x)
    if(p in word_list and p != s):
      matches.add(p)
  return
  

def findAnagramMatches(s,word_list):
  matches = set()
  matches2 = set()
  t1 = threading.Thread(target=calcEvenPermutations,args=(s,word_list,matches))
  t2 = threading.Thread(target=calcOddPermutations,args=(s,word_list,matches2))
  t1.start()
  t2.start()
  t2.join()
  t1.join()

  #calcEvenPermutations(s,word_list,matches)
  #calcOddPermutations(s,word_list,matches2)
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

