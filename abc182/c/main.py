#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode("utf-8").split()
def S(): return sys.stdin.buffer.readline().rstrip().decode("utf-8")
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def SRL(n): return [list(S()) for _ in range(n)]
def MSRL(n): return [[int(i) for i in list(S())] for _ in range(n)]

n=I()
n=str(n)

sum=0
plus1=0
minus1=0

for i in n:
    if int(i)%3==1:
        plus1+=1
    elif int(i)%3==2:
        minus1+=1
    sum+=int(i)

if sum%3==0:
    print(0)
elif sum%3==1:
    if plus1 >=1:
        if len(n)>=2:
            print(1)
        else:
            print(-1)
    elif minus1>=2:
        if len(n)>=3:
            print(1)
        else:
            print(-1)
    else :
        print(-1)
elif sum%3==2:
    if minus1 >=1:
        if len(n)>=2:
            print(1)
        else:
            print(-1)
    elif plus1>=2:
        if len(n)>=3:
            print(1)
        else:
            print(-1)
    else :
        print(-1)
