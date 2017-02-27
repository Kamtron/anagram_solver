import unittest
import anagrams
from itertools import islice

class TestAnagramStuff(unittest.TestCase):

  def test_no_anagram_matches(self):
    s = "ppleaaaa"
    word_list = []
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(0,len(matches))
  
  def test_one_anagram_matches(self):
    s = "pplea"
    word_list = ["apple"]
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(1,len(matches))
  
  def test_dont_match_self(self):
    s = "apple"
    word_list = ["apple"]
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(0,len(matches))

  def test_multiple_matches(self):
    s = "arce"
    word_list = ["race","acre","apple","care"]
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(3,len(matches))

  def test_with_real_word_list(self):
    s = "villnai"
    word_list = anagrams.loadWordList("words.txt")
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(1,len(matches))
 
  def test_with_real_word_list2(self):
    s = "gseg"
    word_list = anagrams.loadWordList("words.txt")
    matches = anagrams.findAnagramMatches(s,word_list)
    self.assertEqual(1,len(matches))

if __name__ == '__main__':
  unittest.main()
