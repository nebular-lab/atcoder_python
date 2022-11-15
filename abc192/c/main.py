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

def g1(x):
    x=str(x)
    x=list(x)
    x.sort(reverse=True)
    x="".join(x)
    return int(x)

def g2(x):
    x=str(x)
    x=list(x)
    x.sort(reverse=False)
    x="".join(x)
    return int(x)

def f(x):
    return int(g1(x)-g2(x))

n,k=LI()

a=[]
a.append(n)

for i in range(k+1):
    a.append(f(a[i]))

print(a[k])

