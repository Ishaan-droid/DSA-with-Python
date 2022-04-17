from xxlimited import new
import numpy as np;

arr2D = np.array([[1,2,3], [4,5,6], [7,8,9]]);

# Inserting elements in array, Axis for 1 is column and for 0 is row
# newArr2D = np.insert(arr2D, 0, [[10,11,12]], axis = 0);
newArr2D = np.append(arr2D, [[4,2,6]], axis=0);

print(newArr2D);

# Accessing element in 2D array
def accessElementIn2DArray(array,rowIndex,colIndex):
    if(rowIndex >= len(array) or colIndex >= len(array[rowIndex])):
        return print('Incorrect Index')
    else:
        return print(array[rowIndex][colIndex]);


# accessElementIn2DArray(newArr2D,1,2)

# Traversing through 2D array
def traverse2DArray(array):
    for arr in array:
        for a in arr:
            print(a)

# traverse2DArray(newArr2D)

# Searching through 2D array
def search2DArray(array,element):
    for arr in array:
        for a in arr:
            if a == element:
                return print(element)

    return print('Element not found')

# search2DArray(newArr2D,6)

# Deletion through 2D array, Axis for 1 is column and for 0 is row
deletedArray = np.delete(newArr2D,0,axis=0)