import heapq
import sys

N = int(sys.stdin.readline())
heap = []


for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x,x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            
#https://littlefoxdiary.tistory.com/3