X = int(input())
result = [0 for _ in range(10000000)]
result[0] = 0
result[1] = 0
result[2] = 1
result[3] = 1
    
for i in range(4, X + 1):
    result[i] = result[i-1] + 1
    
    if i%3 == 0 and result[i] > result[i//3] + 1:
        result[i] = result[i//3] + 1
    if i%2 == 0 and result[i] > result[i//2] + 1:
        result[i] =result[i//2] + 1
print(result[X])