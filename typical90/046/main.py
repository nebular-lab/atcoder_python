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
a=LI()
b=LI()
c=LI()
a_amari=[0]*46
b_amari=[0]*46
c_amari=[0]*46
for elem in a:
    elem%=46
    a_amari[elem]+=1
for elem in b:
    elem%=46
    a_amari[elem]+=1
for elem in c:
    elem%=46
    a_amari[elem]+=1
sum=0
for i in range(46):
    for j in range(46):
        k=(46+46-i-j)%46
        sum+=a_amari[i]+b_amari[j]+c_amari[k]
print(sum)
