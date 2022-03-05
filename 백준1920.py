N = int(input())
N_array = list(map(int, input().split()))
N_array = sorted(N_array)
M = int(input())
M_array = list(map(int, input().split()))


def binary_search(N_array, M_value, start, end):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        if M_value == N_array[mid]:
            return 1
        elif M_value > N_array[mid]:
            return binary_search(N_array, M_value, mid + 1, end)
        else:
            return binary_search(N_array, M_value, start, mid - 1)


for M_index in range(len(M_array)):
    M_value = M_array[M_index]
    print(binary_search(N_array, M_value, 0, len(N_array)-1))