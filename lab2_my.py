word = input("Provide a word to search for vowels: ")

found = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in found:
        found[letter] += 1

for v in found.values():
    print(0, 'was found', v, 'time(s).')

print(found)
print(found.items())
print(found.keys())
print(found.values())