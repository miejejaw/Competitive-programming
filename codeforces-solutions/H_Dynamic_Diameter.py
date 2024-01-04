from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

from sys import setrecursionlimit, stdin
from threading import Thread, stack_size


def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def main():
    n = I()
    adj = defaultdict(list)
    indegree = [0]*(n+1)
    for _ in range(n-1):
        a,b = IL()
        adj[a].append(b)
        adj[b].append(a)



setrecursionlimit(1 << 30)
stack_size(1<<27)
_mt = Thread(target=main)
_mt.start()
_mt.join()