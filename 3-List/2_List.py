# Removing first and last element
def middle(lst):
    arr = []
    for a in range(1,len(lst)-1):
        arr.append(lst[a])
    return arr


answer = middle([12,54,78,45,98,23])

# Sum of diagonal elements
def sumDiagonal(a):
    start = 0
    sum = 0

    for i in range(len(a)):
        sum += a[i][start]
        start += 1

    return sum

answer = sumDiagonal([[1,2,3],[4,5,6],[7,8,9]])

# Find the first and second largest element in list
def firstSecond(givenList):
    max1 = givenList[0]
    for i in range(len(givenList)):
        if givenList[i] > max1:
            max1 = givenList[i]
    
    for a in range(len(givenList)):
        if givenList[a] == max1:
            givenList[a] = 0;
    
    max2 = givenList[0]

    for i in range(len(givenList)):
        if givenList[i] > max2:
            max2 = givenList[i]

    return max1,max2
    
answer = firstSecond([84,85,86,87,85,90,85,83,23,45,84,1,2,0])

# Find missing number
def missingNumber(myList,totalCount):
    for i in range(totalCount):
        if i+1 != myList[i]:
            return i+1

answer = missingNumber([1,2,3,4,6],6)

# Remove Duplicates
def removeDuplicates(myList):
    obj = {}

    for a in myList:
        if a not in obj:
            obj[a] = 1
        else : 
            continue

    return list(dict.keys(obj))

removeDuplicates([1,1,2,2,3,4,5])
