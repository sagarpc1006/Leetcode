# Accept array from user 

# Enter the size of array 
size=int(input("Enter the size of array :"))

A=[None]*size

# Enter elements in array 
for i in range(0,size):
    A[i]=int(input('Enter the element at index %d : '%i))
print('Array is : ',A)

# Input element from user to be search 
index=int(input("Enter the index on which element to be insert : "))
element=int(input("Enter the element to be inserted : "))
for i in range (0,size):
    if (i == index):
        A[i]=element
        break;
print("Updated Array is : ",(A))