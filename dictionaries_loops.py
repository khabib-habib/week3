person2 = {}
person2['name'] = 'Mark'
person2['age'] = 25 
person2['occupation'] ='Engineer'
person2['isSingle'] = False
print(person2)

# looping with keys
for key in person2:
    print(key)
print("===============")

for key in person2.keys():
    print(key)
    print(f"the value of {key} is : {person2[key]} .")

# looping through values with values() method.
for value in person2.values():
    print(value)

# looping through keys and values at the same time with items() method.
for key, value in person2.items():
    print(f"the value of {key} is : {value} .")
    
