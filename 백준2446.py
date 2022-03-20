import sys


input = sys.stdin.readline
N = int(input())
flag = False

start_star = 2*N-1
return_blank = N-2
return_star = 3
for i in range(2*N-1):
    if i>=N:
        arr = ' '*return_blank + '*'*return_star
        return_blank -=1
        return_star += 2
        print(arr)
        continue
    
    blank = ' '*(i)
    star_count = '*'*start_star
    arr = blank + star_count
    start_star -= 2
    print(arr)
    
        
