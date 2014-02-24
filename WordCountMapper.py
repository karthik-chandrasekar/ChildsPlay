#!/usr/bin/python
#coding=utf-8

import sys

class WordCountMapper:
    def __init__(self):
        pass

    def run_main(self):
        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                for word in line.split(','):
                    print "%s\t%s" % (word, 1)
            except:
                print "Exception in WordCountMapper"

if __name__ == "__main__":
    wcm_obj = WordCountMapper() 
    wcm_obj.run_main()

