import words_loader

words = words_loader.load('words.txt')
anagrams = []

name = 'Yarek'
print('{} is the name.'.format(name))
name = name.lower()

name_lst = sorted(name)

for word in words:
    if word != name and len(word) == len(name):
        if name_lst == sorted(word):
            anagrams.append(word)

print(anagrams, sep='\n')
