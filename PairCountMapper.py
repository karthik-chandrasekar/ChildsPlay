#!/usr/bin/python
#coding=utf-8

import itertools,sys

class PairCountMapper:
    def __init__(self):
        self.delimiter = "##$##"

    def run_main(self):
        for line in sys.stdin:
            try:
                if not line:continue
                words = line.strip().split(',')
                words = [word.strip() for word in words if word and word.strip()]
                for pair in itertools.combinations(words[1:], 2):
                    print "%s\t%s" % (self.delimiter.join(pair), 1)
            except:
                continue

if __name__ == "__main__":
    pcm_obj = PairCountMapper() 
    pcm_obj.run_main()
