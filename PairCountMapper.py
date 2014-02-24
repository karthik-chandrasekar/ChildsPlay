#!/usr/bin/python
#coding=utf-8

import itertools,sys

class PairCountMapper:
    
    def __init__(self):
        pass

    def run_main(self):
        
        delimiter = "##$##"
        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                for pair in itertools.combinations(line.split(','), 2):
                    print "%s\t%s" % (delimiter.join(pair), 1)
            except:
                print "Exception in PairCountMapper"

if __name__ == "__main__":
    pcm_obj = PairCountMapper() 
    pcm_obj.run_main()
