#PYTHON 
string = str(input())
left = '{[('
right = '}])'
def check(string):
    stack = []
    for s in string:
        if s in left:
            stack.append(s)
        elif s in right:
            if not stack:
                return 0
            l = stack.pop()
            if right.index(s) != left.index(l):
                return 0
    if stack:
        return 0
    return 1
print(check(string))
