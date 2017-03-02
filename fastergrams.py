from anagrams import loadWordList
import time

def generateKey(s):
  return ''.join(sorted(s))

def addWordToDict(word,d):
  key = generateKey(word)
  if key in d:
    d[key].extend([word])
  else:
    d[key] = [word]
  

def convertWordListToDict(L):
  d = dict()
  for word in L:
    addWordToDict(word,d)
  return d

def findAnagramMatches(s,d):
  key = generateKey(s)
  matches = []
  if key in d:
    for word in d[key]:
      if word != s:
        matches.extend([word])
  return matches

if __name__ == "__main__":
  print("Loading word list")
  word_list = loadWordList("words.txt")
  print("Generating hashes")
  d = convertWordListToDict(word_list)
  print("Ready")
  while(1):
    s = raw_input("Enter a string (or q to quit): ")
    if s == "q":
      break
    begin = time.time()
    matches = findAnagramMatches(s,d)
    end = time.time()
    if(len(matches) > 0):
      print("Matches for "+s+": ")
      for m in matches:
        print(m)
    else:
      print("No matches for "+s)
    print("took " + str(end-begin) + " seconds")
