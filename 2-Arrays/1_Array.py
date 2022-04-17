# CREATE AN ARRAY

from array import *

arr1 = array('i', [3,4,3,2,45,4,3]);
arr2 = array('d', [1.2,6.34,65.3]);
# print(arr1);

# INSERT AN ELEMENT
# arr1.insert(1,69);
# print(arr1)
# arr1.remove(3);

# TRAVERSING THROUGH ARRAY
# for a in arr1:
#     print(a);

# FINDING ELEMENT IN ARRAY

def accessElement(array, index):
    if index >= len(array):
        print('Array out of range.');
    else:
        print(array[index]);

def searchInArray(array,value):
    for a in array:
        if value == a:
            return print('Value is Found', a);
    return print('Value not found.');

searchInArray(arr1, 453);
    