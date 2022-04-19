myDict = {
    'name' : 'Ishaan',
    'age' : 26,
    'yearOfBirth' : 1995
}

# Traversing in a dictionary
def traverseDictionary(dict):
    for key in dict:
        print(key, dict[key])

# traverseDictionary(myDict)

# Deleting an item from dictionary

# To delete a key
# myDict.pop('yearOfBirth') 
# del myDict['yearOfBirth']

# To delete all keys
# myDict.clear()

# To copy a disctionary
newDict = myDict.copy()

# Get an item from dictionary. It will return none if key is not present.
# print(myDict.get('age'))

# in Operator and not in. It Check if key is present in the object or not
# print('name' in myDict)






