# Accept array from user 

# Enter the size of array 
size=int(input("Enter the size of array :"))

A=[None]*size

# Enter elements in array 
for i in range(0,size):
    A[i]=int(input('Enter the element at index %d : '%i))
print(A)