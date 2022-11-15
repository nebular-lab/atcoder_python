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
s=S()
q=I()
dis=LIR(q)

for i in range(q):
    t,a,b=dis[i]
    if t==1:
        swap_a=s[a-1]
        swap_b=s[b-1]
        s_list=list(s)

        s_list[b-1]=swap_a
        s_list[a-1]=swap_b
        s="".join(s_list)
    if t==2:
        swap_pre=s[:n]
        swap_after=s[n:]
        s=swap_after+swap_pre
print (s)

