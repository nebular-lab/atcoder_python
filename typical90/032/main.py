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

a=LIR(n)
m=I()
friendship=[[True for _ in range(n)] for _ in range(n)] #Trueの時には仲がよい
for i in range(m):
    x,y=LI()
    friendship[x-1][y-1]=False
    friendship[y-1][x-1]=False

num=list(range(n))
ptn=list(permutations(num))
bigNum=10000000
ans=bigNum
for p in ptn:
    sum=0
    canFinish=True
    for i in range(n-1):
        now=p[i]
        next=p[i+1]
        if friendship[now][next]==False:
            canFinish=False
            break
        sum+=a[now][i]
    sum+=a[p[n-1]][n-1]
    if canFinish:
        ans=min(ans,sum)
if ans==bigNum:
    print(-1)
else:
    print(ans)

