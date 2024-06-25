class node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def rec(root):
    if root == None:
        return
    
    rec(root.left)
    if root.left is None and root.right is None:
        print(root.value)
    rec(root.right)
    
if __name__ == "__main__":
    n1=node(1)
    root=n1
    n2=node(2)
    n3=node(3)
    n4=node(4)
    n5=node(5)
    n6=node(6)
    n7=node(7)
    n8=node(8)
    n9=node(9)
    n10=node(10)
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n3.left=n6
    n3.right=n7
    n4.left=n8
    n4.right=n9
    n5.left=n10
    li=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
    print("The leaf nodes are:")
    rec(root)


#Top View and Botthom View
'''                           1
                     2                5
              (L)3       4                 6
                      9               7         8(L)
                         10              11
                     14(L)           12
                                        13(L)'''
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,node,HKey):
        self.node=node
        self.Hkey=HKey
def Top_View_Bottom_View(root):
    temp=node_data(root,0)
    Key_dic_T={}
    Key_dic_B={}
    Q=[temp]
    Q.append(None)
    while len(Q)!=0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                Q.append(None)
        else:
            if cur.Hkey not in Key_dic_T.keys():
                Key_dic_T[cur.Hkey]=cur.node.value
            Key_dic_B[cur.Hkey]=cur.node.value
            if cur.node.left!=None:
                temp=node_data(cur.node.left,cur.Hkey-1)
                Q.append(temp)
            if cur.node.right!=None:
                temp=node_data(cur.node.right,cur.Hkey+1)
                Q.append(temp)
    print('Top View Elements')
    for i in sorted(Key_dic_T):
        print(Key_dic_T[i],end=' ')
    print('\nBottom View Elements')
    for i in sorted(Key_dic_B):
        print(Key_dic_B[i],end=' ')
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.right.right=node(6)
    root.left.right.left=node(9)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.left.right.left.right=node(10)
    root.right.right.left.right=node(11)
    root.left.right.left.right.left=node(14)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
    Top_View_Bottom_View(root)
