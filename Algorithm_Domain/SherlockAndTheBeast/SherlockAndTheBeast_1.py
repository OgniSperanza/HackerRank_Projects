#!/bin/python
import sys
t = int(raw_input().strip())
tmp = ""
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n < 3:
        print -1
    elif n % 3 == 0 and n % 5 != 0:
        tmp = ""
        for _ in range(n):
            tmp = tmp + "5"
        print tmp
    elif n % 5 == 0 and n % 3 == 0:
        tmp = ""
        for _ in range(n):
            tmp = tmp + "5"
        print tmp
    elif n % 3 == 1 and (n - 10) >= 0:
        tmp = ""
        i = n - (n - 10)
        for _ in range(n - 10):
            tmp = tmp + "5"
        for _ in range(i):
            tmp = tmp + "3"
        print tmp
    elif n % 3 == 2:
        tmp = ""
        i = n - (n -5)
        for _ in range(n - 5):
            tmp = tmp + "5"
        for _ in range(i):
            tmp = tmp + "3"
        print tmp        
    else:
        print -1
