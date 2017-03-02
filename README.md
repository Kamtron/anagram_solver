### Tis a silly place
I really hate anagrams, so I scripted a tool to solve them.  
I used the silliest possible algorithm:
  - load all possible words into a set
  - check permutations of a given word against the set
Fortunately, looking up something in a set is O(1).
Unfortunately, calculating the permutations is O(n!), where n=len(s)
Long words, such as "prescriptions" have a lot of permutations (6,227,020,800 to be precise), so creating
all of the permutations took some time (some 2000 seconds, even on a shiny new Xeon).

### Sillier than that

Clearly, the next step was to go parallel!
I first tried multithreading, but quickly learned
that the Python gods frown upon such behavior
(see GIL, or Global Interpreter Lock).  There are
some fancy packages out there to help with
managing multiple processes, but I wanted to use
good ole standard python, so I used multiprocessing.

A little bit of refactoring of my functions,
a shared queue, and a loop for launching 
processes, and it was off to the races.  It gave
me about a 2x speedup on 2 cores, and about 5x 
on a 6 core Xeon.  Even the
raspberry pi got some love, with a 3x speedup on
its 4 little ARM cores.

### Finally, some sense

Parallelism is fun and all, but I decided that
it was time for a better algorithm.  I generated
a key for each word in the word list (the key
is independent of letter order).  Then build a 
dictionary based on those keys, and stored a list
of words for each key.  The idea was, that once
the dictionary is built, my lookups are still O(1),
but now I just generate a key instead of 
doing any permutations, so I can cut that part of
the problem from O(n!) --> O(1).

Voila! Now, everything works in constant time!

Now, it takes 3.0e-5 seconds to solve long words
like "prescriptions"

i.e., 75 million times speedup!


wordlist from https://github.com/dwyl/english-words
