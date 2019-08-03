phrase = input("Enter the phrase: ")
# return the vowels used in the phrase
vowels = ['e', 'u', 'i', 'o', 'a']

result = []
for letter in phrase:
    if letter in vowels:
        result.append(letter)
        
print(result)
print("".join(result))

result2 = {'e':0, 'u':0, 'i':0, 'o':0, 'a':0}
