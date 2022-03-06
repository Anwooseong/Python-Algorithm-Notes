#실패
def bfs(start_node): #need_visit 와 visited 큐
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(dic[node])
    return visited
#


def dfs(start_node): #need_visite스택 visited 큐
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop() #스택
        if node not in visited:
            visited.append(node)
            need_visit.extend(dic[node])
    return visited


N, M, V = map(int, input().split())
dic = dict()
for _ in range(M):
    imsi = []
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = [b]
    else:
        imsi.extend(dic.get(a))
        imsi.extend([b])
        dic[a] = imsi
    imsi = []
    if b not in dic:
        dic[b] = [a]
    else:
        imsi.extend(dic.get(b))
        imsi.extend([a])
        dic[b] = imsi
dfs_result = dfs(V)
bfs_result = bfs(V)
for i in range(len(dfs_result)):
    print(dfs_result[i], end=' ')
print()
for i in range(len(bfs_result)):
    print(bfs_result[i], end=' ')