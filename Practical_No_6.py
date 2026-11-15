class myqueue:
    def __init__(self,size):
        self.A=[None]*size
        self.front=0
        self.rear=-1
        self.size=size


def isEmpty(self):
    if self.front > self.rear:
        return True 
    else:
        return False


def isFull(self):
    if self.rear == self.size-1:
        return True 
    else:
        return False


def enqueue(self,X):
    if not self.isFull():
        self.rear=self.rear+1
        self.A[self.rear]=X
        print('Element enqueued successfully')
    else :
        print('Stack Overflow')

def dequeue(self,X):
    if not self.isFull():
        X=self.A[self.front]
        self.front=self.front+1
        return X 
    else:
        return None


def getfront(self) :
    if not self.isEmpty() :
        X = self.A[self.front]
        return X
    else :
        print("queue Underflow error\\n")
        return None

def getfront(self):
    if not self.isEmpty():
        return self.A[self.front]
    else : 
        return None
def Main():
    s1 = myqueue(5)
    while True :
        print("\t\t1 : enqueue")
        print("\t\t2 : dequeue")
        print("\t\t3 : Empty")
        print("\t\t4 : Full")
        print("\t\t5 : getfront")
        print("\t\t6 : Exit")
    ch = int(input("Enter ur choice : "))
    if ch == 1 :
        X = int(input("Enter element to enqueue on queue : "))
        s1.enqueue(X)
    elif ch == 2 :
        X = s1.dequeue()
        if X != None :
            print("Element %d dequeueed from the queue"%X)
    elif ch==3:
        if s1.isEmpty() == True:
            print("queue is Empty\\n")
        else:
            print("queue is not Empty\\n")
    elif ch == 4 :
        if s1.isFull() == True :
            print("queue is Full\\n")
        else :
            print("queue is not Full\\n")
    elif ch == 5 :
        X = s1.getfront()
        if X != None :
            print("Element %d present on rear of queue"%X)
    elif ch == 6 :
        print("End of program\\n")
        breakpoint
    else :
        print("Invalid choice !! TRy again\\n")
Main()
quit()
            

