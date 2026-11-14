class mystack:
    def __init__(self,max):
        self.A=[None]*max
        self.top=-1
        self.size=max
        

def isEmpty(self) : 
    if self.top == -1 : 
        return True 
    else : 
        return False 

    
def isFull(self) : 
    if self.top == self.size-1 : 
        return True 
    else : 
        return False

 
def push(self,X) : 
    if not self.isFull() : 
        self.top = self.top + 1 
        self.A[self.top] = X 
        print("Element %d pushed on the stack\n"%X) 
    else : 
        print("Stack Full Error\n")


def pop(self):
    if not self.isEmpty():
        X=self.A[self.top]
        self.top=self.top-1
        return X
    else :
        print()


def peek(self) : 
    if not self.isEmpty() :    
        X = self.A[self.top]     
        return X 
    else : 
        print("Stack EmptyError\n") 
        return None


def Main() : 
    s1 = mystack(5) 
    while True : 
        print("\t\t1 : Push") 
        print("\t\t2 : Pop") 
        print("\t\t3 : Empty") 
        print("\t\t4 : Full") 
        print("\t\t5 : Peek") 
        print("\t\t6 : Exit") 
        ch = int(input("Enter ur choice : ")) 
        if ch == 1 : 
            X = int(input("Enter element to push on stack : ")) 
            s1.push(X)
        elif ch == 2 : 
            X = s1.pop() 
            if X != None : 
                print("%d element poped from the stack"%X) 
        elif ch == 3 : 
            if s1.isEmpty() : 
                print("Stack is empty\n") 
            else : 
                print("Stack is not empty\n") 
        elif ch == 4 : 
            if s1.isFull() : 
                print("Stack is Full\n") 
            else : 
                print("Stack is not Full\n") 
        elif ch == 5 : 
            X = s1.peek() 
            if X != None : 
                print("%d element is topmost element"%X) 
        elif ch == 6 : 
            print("End\n") 
            break 
        else : 
            print("Invalid choice ! Try again\n") 
Main() 
quit()