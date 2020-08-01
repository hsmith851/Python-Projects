# Python3 program to find sum in Nth group

# Check if given array is Monotonic
def isMonotonic(A):
    return (all (A[i] <= A[i + 1] for i in range (len (A) - 1)) or
            all (A[i] >= A[i + 1] for i in range (len (A) - 1)))



# Driver program
A = []  # input/output
n = int (input ("Enter number of elements : "))

for i in range (0, n):
    element = int (input ( ))
    A.append (element)  # adding the element a

    n = len (A)
# Print required result
print (isMonotonic (A))