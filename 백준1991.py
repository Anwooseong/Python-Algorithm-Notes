N = int(input())
binary_tree = dict()
for i in range(N):
    current, left, right = input().split()
    binary_tree[current] = [left, right]

def prefix(current):
    if current == '.':
        return
    print(current,end='')
    prefix(binary_tree[current][0])
    prefix(binary_tree[current][1])
    
     
def infix(current):
    if current == '.':
        return
    infix(binary_tree[current][0])
    print(current,end='')
    infix(binary_tree[current][1])
    
def postfix(current):
    if current == '.':
        return
    postfix(binary_tree[current][0])
    postfix(binary_tree[current][1])
    print(current,end='')

prefix('A')
print()
infix('A')
print()
postfix('A')