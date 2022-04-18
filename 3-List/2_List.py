def middle(lst):
    arr = []
    for a in range(1,len(lst)-1):
        arr.append(lst[a])
    return arr


answer = middle([12,54,78,45,98,23])

def sumDiagonal(a):
    start = 0
    sum = 0

    for i in range(len(a)):
        sum += a[i][start]
        start += 1

    return sum

answer = sumDiagonal([[1,2,3],[4,5,6],[7,8,9]])
