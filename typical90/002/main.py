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
if n%2==1:
    print("")
    exit()

for bit in range(2**n-1,0,-1):
    sum=0
    isOK=True
    ans=""
    for i in range(n):
        if bit&(1<<i):
            sum-=1
            ans+="("
        else:
            sum+=1
            ans+=")"
        if (sum<0):
            isOK=False
    if sum!=0:
        isOK=False
    if isOK:
        reversedAnsList=list(reversed(ans))
        print("".join(reversedAnsList))


