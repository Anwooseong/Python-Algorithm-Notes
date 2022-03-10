import sys


N, M = map(int, sys.stdin.readline().split())
pocketmon_list_number = {}
for i in range(N):
    pocketmon_list_number[input()] = i+1
pocketmon_list_name = list(pocketmon_list_number.keys()) #이름
for _ in range(M):
    print_pocketmon= sys.stdin.readline().rstrip()
    if print_pocketmon.isdigit():
        print(pocketmon_list_name[int(print_pocketmon) - 1])
    else:
        print(pocketmon_list_number[print_pocketmon])
        