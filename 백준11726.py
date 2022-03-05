def tile(num):
    result = [index for index in range(num+1)]
    if num > 3:
        for number in range(4, num+1):
            result[number] = (result[number-1]+result[number-2])%10007
    return result[num]

n = int(input())
print(tile(n))