import sys


input = sys.stdin.readline
num_list = [0]*9
max_index = 0
max_value = 0
for i in range(len(num_list)):
    num_list[i] = int(input())
    if max_value < num_list[i]:
        max_index = i+1
        max_value = num_list[i]
print(max_value)
print(max_index)

        