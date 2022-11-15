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
a_list=LI()
double_count=[0]*n
triple_count=[0]*n
count=0
for i,a in enumerate(a_list):
    elem=a
    while elem%2==0:
        elem/=2
        double_count[i]+=1
        count+=1
    while elem%3==0:
        elem/=3
        triple_count[i]+=1
        count+=1
    a_list[i]=int(elem)
first=a_list[0]
# print(*a_list)
for a in a_list:
    if first!=a:
        print(-1)
        exit()

print(count-min(double_count)*n-min(triple_count)*n)

