class bst_node:
    def __init__(self,d):
        self.lc=None
        self.data=d
        self.rc=None 


class mybst:
    def __init__(self):
        self.root=None


    def insert_bst(self,node) :
        if self.root == None :
            self.root = node
        else :
            par = self.root
            while True :
                if node.data < par.data :
                    if par.lc == None :
                        par.lc = node
                        break
                    else :
                        par = par.lc
                else :
                    if par.rc == None :
                        par.rc = node
                        break
                    else :
                        par = par.rc

    def create_bst(self):
        n=int(input('Enter total no of nodes in BST : '))
        for i in range(n):
            data=int(input("Enter data in Node %d: "%(i+1)))
            node = bst_node(data)
            self.insert_bst(node)
    print("\nBST Created Successfully")


    def inorder(self,node) :
        if node != None :
            self.inorder(node.lc)
            print(node.data," ",end="")
            self.inorder(node.rc)

    def preorder(self,node):
        if node!=None:
            print(node.data," ",end="")
            self.preorder(node.lc)
            self.preorder(node.rc)

    def postorder(self,node):
        if node!=None:
        
            self.postorder(node.lc)
            self.postorder(node.rc)
            print(node.data," ",end="")

    def traverse_bst(self):
        print('Inorder Traversal of BST : ',end="")
        self.inorder(self.root)
        print('Preorder Traversal of BST : ',end="")
        self.preorder(self.root)
        print('Postorder Traversal of BST : ',end="")
        self.postorder(self.root)


def Main():
    b1 = mybst()
    while True :
        print("\t\t1 : Create BST")
        print("\t\t2 : Traverse BST")
        print("\t\t3 : Exit")
        ch = int(input("Enter your choice : "))
        if ch == 1 :
            b1.create_bst()
        elif ch == 2 :
            b1.traverse_bst()
        elif ch == 3 :
            print("End\n")
            break
        else :
            print("Invalid choice ! Try again")
Main()
quit()