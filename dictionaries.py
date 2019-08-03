# dictionaries go by Key and Value pair
person1 = {'name':'John',
             'age':30}

print(person1['name']) # accessing the values by keys
print(person1)

# adding objects to the dictionary
person1['occupation'] = 'QA'
person1['isSingle'] = True
print(person1)

person2 = {}
person2['name'] = 'Mark'
person2['age'] = 25 # int(input("Enter the age of person2: "))
person2['occupation'] ='Engineer'
person2['isSingle'] = False
print(person2)

person2['age'] += 1 # this is the same as >> person2['age'] = person2['age'] + 1
person2['occupation'] = 'Sr. Engineer'
person2['location'] = 'Brooklyn'
print(person2)

del person2['location'] # this deletes the key/value pair from the person2 dictionary
print(person2)
print(person2['name'].upper() )
