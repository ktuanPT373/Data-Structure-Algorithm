#PYTHON 
#PYTHON 
#PYTHON 
#PYTHON 
class List:
    def __init__(self,a):
        self.a = arr


    def addlast(self,n):
        if n not in self.a:
            self.a.append(n)

    def addfirst(self,n):
        if n not in self.a:
            self.a = [n] + self.a

    def addafter(self,u,v):
        temp = 0
        if u not in self.a:
            for i in range(len(self.a)):
                if self.a[i] == v:
                    temp = i
                    break
            self.a = self.a[:temp+1]+[u]+self.a[temp+1:]

    def addbefore(self,u,v):
        temp = 0
        if u not in self.a:
            for i in range(len(self.a)):
                if self.a[i] == v:
                    temp = i
                    break
            self.a = self.a[:temp]+[u]+self.a[temp:]

    def remove(self,k):
        if k in self.a:
            self.a.remove(k)

    def reverse(self):
        self.a = self.a[::-1]
    def __str__(self):
      return ' '.join(str(i) for i in self.a)
n = int(input())
arr = list(map(int,input().split()))
im = List(arr)
while True:
  command = input().split()
  if command[0] == "addlast":
      im.addlast(int(command[1]))
  elif command[0] == "addfirst":
      im.addfirst(int(command[1]))
  elif command[0] == "addafter":
      im.addafter(int(command[1]), int(command[2]))
  elif command[0] == "addbefore":
      im.addbefore(int(command[1]), int(command[2]))
  elif command[0] == "remove":
      im.remove(int(command[1]))
  elif command[0] == "reverse":
      im.reverse()
  elif command[0] == "#":
      break

print(im)
