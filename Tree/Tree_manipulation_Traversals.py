class Node:
    def __init__(self,id):
        self.id = id
        self.children = []
class Tree:
    def __init__(self):
        self.root = None
    def MakeRoot(self,u):
        self.root = Node(u)
    def findNode(self,node,u):
        if node.id == u:
            return node
        for child in node.children:
            result = self.findNode(child,u)
            if result:
                return result
        return None
    def Insert(self,u,v):
        if not self.findNode(self.root,u) and self.findNode(self.root,v):
            v_node = self.findNode(self.root,v)
            v_node.children.append(Node(u))
    def preOrder(self,node,result):
        if node:
            result.append(node.id)
            for child in node.children:
                self.preOrder(child,result)
    def InOrder(self, node, result):
      if node:
          if len(node.children) > 1:
              self.InOrder(node.children[0], result)
              result.append(node.id)
              for child in range(1, len(node.children)):
                  self.InOrder(node.children[child], result)
          elif len(node.children) == 1:
              result.append(node.children[0].id)
              result.append(node.id)
          else:
              result.append(node.id)
    def postOrder(self,node,result):
        if node:
            for child in node.children:
                self.postOrder(child,result)
            result.append(node.id)

def process_data(input_data):
    tree = Tree()
    lines = input_data.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line == '*':
            break

        command, *args = line.split()
        if command == 'MakeRoot':
            tree.MakeRoot(int(args[0]))
        elif command == 'Insert':
            tree.Insert(int(args[0]), int(args[1]))
        elif command == 'PreOrder':
            result = []
            tree.preOrder(tree.root, result)
            print(' '.join(map(str, result)))
        elif command == 'InOrder':
            result = []
            tree.InOrder(tree.root, result)
            print(' '.join(map(str, result)))
        elif command == 'PostOrder':
            result = []
            tree.postOrder(tree.root, result)
            print(' '.join(map(str, result)))

input_data = ''
while True:
    line = input()
    if line == '*':
        break
    input_data += line + "\n"
process_data(input_data)
