from array import *

# 1. Create an Array and traverse
arr1 = array('i', [1,2,3,4,5,6]);

for a in arr1:
    print(a);

# 2. Accessing individual elements through index
arr1[3];

# 3. Append any value to the array
arr1.append(56);

# 4. Insert value in array
arr1.insert(2,67);

# 5. Extend an array
arr2 = array('i',[7,8,9]);
arr1.extend(arr2);

# 6. Remove an element in array
arr1.remove(5);

# 7. Remove last element in array
arr1.pop();

# 8. Get index of an element
print(arr1.index(2));

# 9. Reverse the array
arr1.reverse();

# 10. Check number of occurances of an element in an array
arr1.count(4);

# 11. Slice elements of an array
arr1[0:3];