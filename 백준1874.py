count = 0
imsi = list()
n = int(input())
n_list = list()
result = list()
result_false = True
for i in range(n):
    n_list.append(int(input()))
while len(n_list) != 0:
    while count < n_list[0]:
        count += 1
        imsi.append(count)
        result.append('+')

    if imsi[-1] == n_list[0]:
        imsi.pop()
        result.append('-')
        del n_list[0]
    else:
        result_false = False
        break
if result_false != True:
    print('NO')
else:
    for value in result:
        print(value)
