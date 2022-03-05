import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

def postfix(data):
    if data.left != None:
        postfix(data.left)
    if data.right != None:
        postfix(data.right)
    print(data.value)

head = list()
while True:
    try:
        head.append(int(sys.stdin.readline()))
    except:
        break
binary_tree = NodeMgmt(Node(head[0]))
for num in head[1:]:
    binary_tree.insert(num)
postfix(binary_tree.head)
