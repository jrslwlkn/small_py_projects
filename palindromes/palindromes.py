import words_loader

words = words_loader.load('words.txt')
palindromes = []

for word in words:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print(*palindromes, sep='\n')
