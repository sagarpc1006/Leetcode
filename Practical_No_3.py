class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
 
def create_list(): 
    head = None 
    temp = None 
    n = int(input("Enter the number of nodes : ")) 
    for i in range(n): 
        data = int(input("Enter data for node %d : " % (i + 1))) 
        newnode = Node(data) 
        if head == None: 
            head = newnode 
            temp = newnode 
        else: 
            temp.next = newnode 
            temp = newnode 
    print("Singly Linked List created successfully") 
    return head 
 
def traverse_list(head): 
    if head == None: 
        print("Linked List is empty") 
        return 
    temp = head 
    print("Linked List : ", end="") 
    while temp != None: 
        print(temp.data, end="") 
        if temp.next != None: 
            print(" -> ", end="") 
        temp = temp.next 
    print(" -> NULL") 
    print("Linked List traversed successfully") 

def main(): 
    head = None 
    while True: 
        print("1. Create Singly Linked List") 
        print("2. Traverse Singly Linked List") 
        print("3. Exit") 
        ch = int(input("Enter your choice : ")) 
        if ch == 1: 
            head = create_list() 
        elif ch == 2: 
            traverse_list(head) 
        elif ch == 3: 
            print("End of Program !! Goodbye") 
            break 
        else: 
            print("Invalid choice") 
main() 
