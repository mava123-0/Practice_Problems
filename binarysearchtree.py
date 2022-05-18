class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.parent=None
        self.key=0
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        
class BST:
    def __init__(self):
        self.root=None
    def insert(self,key,v):
        nw=Node(key)  
        if(v==None and v==self.root):
            self.root=nw
        if(v==None and v!=self.root):
            return
        if(v.key>=key):
            if(v.left==None):
                v.left=nw
                nw.parent=v
                return
            self.insert(key,v.left)
        if(v.key<=key):
            if(v.right==None):
                v.right=nw
                nw.parent=v
                return
            self.insert(key,v.right)
    def inorder(self,v):
        if(v==None):
            return
        self.inorder(v.left)
        print(v.key,end=",")
        self.inorder(v.right)
            
def main():
    bst=BST()
    print("Enter Number of Nodes in BST: ",end="")
    n=int(input())
    print()
    print("Enter the Values: ")
    x=input().split(" ")
    for i in range(n):
        bst.insert(int(x[i]),bst.root)
    print("The Inorder Travseral is: ",end="")
    bst.inorder(bst.root)
    print()
    print("The Root is: ",bst.root.key)
    
    
if __name__=='__main__':
    main()