class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def MakeRoot(self, u):
        self.root = Node(u)

    def findNode(self, node, u):
        if node.id == u:
            return node
        for child in node.children:
            result = self.findNode(child, u)
            if result:
                return result
        return None

    def Insert(self, u, v):
        u_node = self.findNode(self.root, u)
        v_node = self.findNode(self.root, v)

        if not u_node and v_node:
            v_node.children.append(Node(u))

    def Height(self, u):
        node = self.findNode(self.root, u)
        return self.calculateHeight(node)

    def calculateHeight(self, node):
        if not node.children:
            return 1
        height = 0
        for child in node.children:
            height = max(height, self.calculateHeight(child))
        return 1 + height

    def Depth(self, u):
        node = self.findNode(self.root, u)
        return self.calculateDepth(node,self.root)
    
    def calculateDepth(self,node,stack=[],path=1):
        if node == self.root.id:
            return 1
        stack.append(self.root.id)
        while stack:
            new = stack.pop()
            if new == node:
                return path
            else:
                path += 1
                for child in node.children:
                    if child.id:
                        stack.append(child.id)
        return path
            
def process_data(input_data):
    tree = Tree()
    lines = input_data.strip().split('\n')

    for line in lines:
        if line == '*':
            break

        command, *args = line.split()
        if command == 'MakeRoot':
            tree.MakeRoot(int(args[0]))
        elif command == 'Insert':
            tree.Insert(int(args[0]), int(args[1]))
        elif command == 'Height':
            result = tree.Height(int(args[0]))
            print(result)
        elif command == 'Depth':
            result = tree.Depth(int(args[0]))
            print(result)

input_data = ''
while True:
    line = input()
    if line == '*':
        break
    input_data += line + '\n'
process_data(input_data)
