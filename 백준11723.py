import sys


M = int(input())
S = set()
for _ in range(M):
    arr = sys.stdin.readline().strip().split()
    if len(arr) == 1:
        if arr[0] == 'all':
            S = set([i for i in range(1, 21)])
        if arr[0] == 'empty':
            S = set()
    else:
        num = int(arr[1])
        if arr[0] == 'add':
            S.add(num)
        elif arr[0] == 'remove':
            S.discard(num)
        elif arr[0] == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif arr[0] == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
