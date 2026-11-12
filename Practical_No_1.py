# Array operations

def create_array():
    size=int(input('Enter the size of array : '))
    A=[0]*size
    for i in range(size):
        A[i]=int(input('Enter the element at index %d :'%(i)))
    return A


def display_array(A):
    print('Array elements are : ')
    for i in A:
        print(i,end=" ")
    print()


def insert_element(A):
    element=int(input('Enter the element to be inserted : '))
    position=int(input('Enter the position at which element to be inserted : '))
    A.append(0)
    for i in range(len(A)-1,position,-1):
        A[i]=A[i-1]
    A[position]=element
    print('Updated array is : ')
    display_array(A)
    return A


def delete_element(A):
    position=int(input('Enter the position at which element to be deleted : '))
    for i in range(position,len(A)-1):
        A[i]=A[i+1]
    A.pop()
    print('Updated array is : ')
    display_array(A)
    return A


def update_element(A):
    old_value=int(input('Enter the element to be updated'))
    new_value=int(input('Enter the new value'))
    for i in range(len(A)):
        if A[i]==old_value:
            A[i]=new_value
            break
    print('Updated array is : ')
    display_array(A)
    return A


def search_element(A):
    element=int(input('Enter the element to be search : '))
    found=False
    for i in A:
        if element==i:
            found=True
            break
    if found==True:
        print('Element found')
    else:
        print('Element not found')


def main():
    A=[]
    while True:
        print("1: Create Array")         
        print("2: Display Array")         
        print("3: Insert Element")         
        print("4: Delete Element")         
        print("5: Update Element")         
        print("6: Search Element")         
        print("7: Exit") 
        ch=int(input('Enter the choice : '))
        if ch == 1:
            A=create_array()
        elif ch==2:
            display_array(A)
        elif ch==3:
            insert_element(A)
        elif ch==4:
            delete_element(A)
        elif ch==5:
            update_element(A)
        elif ch==6:
            search_element(A)
        elif ch==7:
            break
        else :
            print('Invalid Choice')

main()