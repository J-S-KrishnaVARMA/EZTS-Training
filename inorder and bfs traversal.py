graph_dict={
    1:[(1,2,0),(1,3,0)],
    2:[(2,1,0),(2,7,0)],
    3:[(3,1,0),(3,5,0),(3,6,0)],
    4:[(4,7,0),(4,8,0)],
    5:[(5,3,0),(5,7,0)],
    6:[(6,3,0),(6,8,0)],
    7:[(7,2,0),(7,5,0),(7,4,0)],
    8:[(8,4,0),(8,6,0)]
}
x=(1,2,3,4,5,6,7,8,9)
y=False
visited=dict.fromkeys(x,y)
stack=[]

def dfs(g,start,visited,stack):
    if visited[start]==False:
        stack.append(start)
        visited[start]=True
    else :
        return
    for i in g[start]:
        dfs(g,i[1],visited,stack)
    print(stack.pop())

dfs(graph_dict,1,visited,stack)


class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def insert(root,node):
    if root.val<node.val:
        if root.right==None:
            root.right=node
        else:
            insert(root.right,node)
    elif root.val>node.val:
      if root.left==None:
            root.left=node
      else:
          insert(root.left,node)
def pri(root):
    if root is None:
        return
    pri(root.left)
    print(root.val)
    pri(root.right)

def pr(root):
    li=[]
    if root is None:
        return
    li.append(root)
    li.append(None)
    while len(li)>1:
        node=li.pop(0)

        if node==None:
            print()
            li.append(node)
        else:
            print(node.val,end=" ")
            if node.left!=None:
                li.append(node.left)
            if node.right!=None:
                li.append(node.right)
                
    
            
l=[4,5,6,1,2,10,66]
if len(l)!=0:
    rootNode=Node(l[0])
l.pop(0)
for i in l:
    newNode=Node(i)
    insert(rootNode,newNode)
print("The tree is:")
pri(rootNode)
print("BFS is:")
pr(rootNode)
