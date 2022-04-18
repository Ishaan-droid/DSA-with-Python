# Max Product of 2 integers in array

arr = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21];

def findMax(val):
    for i in range(len(arr)-1):
        if arr[i+1] > val and i+1 < len(arr):
            val = arr[i+1]
    return val

def maxProduct(arr):
    max1 = findMax(arr[0])
    arr[arr.index(max1)] = 0
    max2 =findMax(arr[0])
    return max1 * max2

print(maxProduct(arr))

    