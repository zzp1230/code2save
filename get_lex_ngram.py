#!/usr/bin/python
# -*- coding:utf8 -*-

import sys
import math
import random
import re

if(len(sys.argv) != 4):
	print "usage: python get_lex_ngram.py han_and_pin.all pin.all name"
	print "output: name.lex name.ngram "
	sys.exit(1)

han = open("/Users/alpha/NLP/han2pin/umdhmm/umdhmm-v1.02/%s" % sys.argv[1],'rb')
pin = open("/Users/alpha/NLP/han2pin/umdhmm/umdhmm-v1.02/%s" % sys.argv[2],'rb')

lex = file("/Users/alpha/NLP/han2pin/umdhmm/umdhmm-v1.02/%s.lex" % sys.argv[3],'w')
ngram = file("/Users/alpha/NLP/han2pin/umdhmm/umdhmm-v1.02/%s.ngram" % sys.argv[3],'w')

dict_han = {}
dict_pin = {}

# calculate: lex
for line in han.readlines():
    line = line.split(" ")
    length = len(line) / 2
    for i in range(length):
        str = line[i] + "\t" + line[i+length]
        if str in dict_han:
            dict_han[str] += 1
        else:
            dict_han[str] = 1

for k in dict_han.keys():
    strs = k + "\t" + "%d" % dict_han[k]
    print >> lex, strs


# calculate: ngram
for line in pin.readlines():
    line = line.split(" ")
    for i in range(len(line)):
        if line[i] in dict_pin:
            dict_pin[line[i]] += 1
        else:
            dict_pin[line[i]] = 1

	if(i < (len(line) -1)):
	    str = line[i] + "\t" + line[i + 1]
	    if str in dict_pin:
		dict_pin[str] += 1
       	    else:
            	dict_pin[str] = 1

for k in dict_pin.keys():
    strs = k + "\t" + "%d" % dict_pin[k]
    print >> ngram,strs

# close files
han.close()
pin.close()
lex.close()
ngram.close()
