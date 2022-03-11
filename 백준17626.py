import math
import sys


input = sys.stdin.readline
n = int(input())
count = 0


while n >= 2:
    count += 1
    print(n, count)
    n = n - int(math.sqrt(n))**2
print(count)