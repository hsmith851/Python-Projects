# Find sum of elements in given array
def _sum(arr, n):
    # return sum using sum
    # inbuilt sum() function
    return (sum (arr))


# display sum
arr = []  # input/output
n = int (input ("Enter number of elements : "))

for i in range (0, n):
    element = int (input ( ))
    arr.append (element)  # adding the element a

    n = len (arr)
    ans = _sum (arr, n)

print (arr)
print ('Sum of the array is ', ans)
