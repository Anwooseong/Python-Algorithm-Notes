N = int(input())
X = list(map(int, input().split()))
ans = [0 for _ in range(len(X))]

X_set = sorted(set(X))  #X를 집합을 만들어 중복을 제거하고 리스트 정렬함
X_dict = {X_set[i]:i for i in range(len(X_set))}
for i in X:
    print(X_dict[i], end=' ')