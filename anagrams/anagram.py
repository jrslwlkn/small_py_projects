import words_loader

words = words_loader.load('words.txt')
anagrams = []

name = str(input('Enter a name to find anagrams: '))
print('{} is the name.'.format(name))
name = name.lower()

name_lst = sorted(name)

for word in words:
    if word != name and len(word) == len(name):
        if name_lst == sorted(word):
            anagrams.append(word)

if len(anagrams):
    print('Here are the found anagrams:\n{}'.format(*anagrams), sep='\n')
else:
    print('Oops, your name must be quite unique!')
