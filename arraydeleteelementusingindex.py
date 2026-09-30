# Accept array from user 

# Enter the size of array 
size=int(input("Enter the size of array :"))

A=[None]*size

# Enter elements in array 
for i in range(0,size):
    A[i]=int(input('Enter the element at index %d : '%i))
print('Array is : ',A)

# Input element from user to be search 
index=int(input("Enter the index which to be deleted : "))

if 0 <= index < len(A) :
    A.pop(index)
    print("Element removed successfully")
    print("Updated array will be : ",A)
else : 
    print("Index out of the bound")