# 입력받기
N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))
N_arr.sort()
#처음에 틀린이유는 M_arr를 정렬하였기 때문 -> 정렬을 하기 않고 그 target값으로 이진 탐색을 돌려 0과 1의 값이 나와야하기때문

#이진 탐색으로 시간 단축
def binary_search(array, target, low, high):
    if(low > high):
        return None

    mid = (low + high) // 2
    if(array[mid] == target):
        return mid
    elif (array[mid] > target):
        return binary_search(array, target, low, mid - 1)
    else: #array[mid] < target
        return binary_search(array, target, mid + 1, high)

#python null객체는 None으로 표현
for value in M_arr:
    if(binary_search(N_arr, value, 0, N-1) != None):
        print(1, end=' ')
    else:
        print(0, end=' ')