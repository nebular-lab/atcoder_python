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

h,w=LI()

a=LIR(h)
row_sum=[]
for i in range(h):
    row=0
    for j in range(w):
        row+=a[i][j]
    row_sum.append(row)
col_sum=[]
for j in range (w):
    col =0
    for i in range(h):
        col+=a[i][j]
    col_sum.append(col)
ans=[[]for _ in range(h)]
for i in range(h):
    for j in range (w):
        ans[i].append(row_sum[i]+col_sum[j]-a[i][j])

for i in range(h):
    print(*ans[i])
