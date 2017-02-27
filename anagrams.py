from itertools import permutations, islice
import threading
import multiprocessing
import time
from math import factorial

def calcPermutations(s,word_list,work_unit,total_units,match_q):
  n = factorial(len(s))
  matches = set()
  for x in islice(permutations(s),work_unit,n,total_units):
    p = ''.join(x)
    if(p in word_list and p != s):
      matches.add(p)
  match_q.put(matches)
  return
  

def findAnagramMatches(s,word_list):
  match_queue = multiprocessing.Queue()
  processes = []
  nproc = 1
  for i in range(nproc):
    processes.append(multiprocessing.Process(target=calcPermutations,args=(s,word_list,i,nproc,match_queue)))
    processes[i].start()

  matches = set()
  for i in range(nproc):
    processes[i].join()
  for i in range(nproc):
    matches = matches.union(match_queue.get())

  return matches

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

