#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    size = 1
    for i in range(0,n):
        if i % 2 == 0:
            size = size * 2
        else:
            size = size + 1
        n = n -1
    print size
