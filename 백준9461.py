T = int(input())
result = [0]*101
result[1] = 1
result[2] = 1
result[3] = 1
def triangle(num):
    for number in range(4, num+1):
        result[number] = result[number - 3] + result[number - 2]
    return result[num]
for i in range(0,T):
    N = int(input())
    print(triangle(N))