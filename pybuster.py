import urllib2
import threading
import Queue
import urllib

#TODO: Build in YAML/Click support and refactor. Current code is quick and dirty. Refactoring to make more Pythonic and OO.

threads = 50
target_url = "http://testpho.vulnweb.com"
wordlist_file = "tmp/all.txt" # from SVNDigger
resume = None
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:8.0a1) Gecko/20110720 Firefox/8.0a1"

def build_wordlist(wordlist_file):
"""  Read in a wordlist and then iterate over each line in the file.
when the file is parsed the queue of words for the actual brute forcing is pulled. """

  # read in the wordlist, binary mode
  fd = open(wordlist_file, "rb") # 
  raw_words = fd.readlines()
  fd.close
  
  found_resume = False
  words = Queue.Queue()
  
  for word in raw_words:

    words = word.rstrip()

    if resume is not None:

      if found_resume:
        words.put(word)

      else:
        if word == resume:
          found_resume = True
          print "Resuming wordlist from: $s" % resume

    else:
         words.put(word)
        
  return words

