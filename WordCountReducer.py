#!/usr/bin/python
#coding=utf-8

import sys

class WordCountReducer:
    def __init__(self):
        pass

    def run_main(self):
        current_pair = None
        current_count = 0

        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
            
                pair, count = line.split("\t")
                count = int(count)
            
                if pair == current_pair:
                    current_count += count
                else:
                    if current_pair:
                        print "%s\t%s" % (current_pair, current_count)
                    current_pair = pair
                    current_count = count
            except:
                print "Exception in WordCountReducer"                

        if current_pair:
            print "%s\t%s" % (current_pair, current_count)
            
if __name__ == "__main__":
    wcr_obj = WordCountReducer()
    wcr_obj.run_main() 

