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


def eight_to_ten(x):
    return int(str(x),8)

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

n,k=LI()
if n==0:
    print(0)
    exit()

for _ in range(k):

    nine=base10int(eight_to_ten(n),9)
    list_nine=list(nine)
    for i,elem in enumerate(list_nine):
        if elem=="8":
            list_nine[i]="5"
    n="".join(list_nine)
print(n)
