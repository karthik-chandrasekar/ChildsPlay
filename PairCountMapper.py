#!/usr/bin/python
#coding=utf-8

import itertools,codecs,sys

class PairCountMapper:
    def __init__(self):
        self.delimiter = ","

    def run_main(self):
        for line in sys.stdin:
            if not line:continue
            words = line.strip().split(',')
            for pair in itertools.combinations(words[1:], 2):
                print "%s\t%s" % (self.delimiter.join([pair[0].strip(), pair[1].strip()]), 1)
            

if __name__ == "__main__":
    pcm_obj = PairCountMapper() 
    pcm_obj.run_main()
