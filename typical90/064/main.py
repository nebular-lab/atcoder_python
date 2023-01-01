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

n,q=LI()

a=LI()
b=[]
for i in range(n-1):
    b.append(a[i+1]-a[i])

sum=0
for j in b:
    sum+=abs(j)


for i in range(q):
    l,r,v=LI()
    if l!=1:
        pre=b[l-2]
        b[l-2]+=v
        after=b[l-2]
        sum-=abs(pre)
        sum+=abs(after)
    if r!=n:
        pre=b[r-1]
        b[r-1]-=v
        after=b[r-1]
        sum-=abs(pre)
        sum+=abs(after)


    print(sum)
