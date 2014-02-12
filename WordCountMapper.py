#!/usr/bin/python
#coding=utf-8

import sys

class WordCountMapper:
    def __init__(self):
        pass

    def run_main(self):
        for line in sys.stdin:
            try:
                if not line:continue
                words = line.strip().split(',')
                words = [word.strip() for word in words if word and word.strip()]
                for word in words:
                    print "%s\t%s" % (word, 1)
            except:
                continue

if __name__ == "__main__":
    wcm_obj = WordCountMapper() 
    wcm_obj.run_main()

