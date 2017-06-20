#!/bin/python

import sys
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    x = n
    while(x % 3 != 0): 
        x = x -5 
    if(x < 0): 
        print "-1" 
    else: 
        print x * "5" + (n - x) * "3"
