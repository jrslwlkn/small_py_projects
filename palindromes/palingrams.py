import words_loader

words = words_loader.load('words.txt')


def find_palingrams():
    palingrams = []
    for word in words:
        end = len(words)
        word_rev = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == word_rev[:end-i] and word_rev[end-i:] in words:
                    palingrams.append((word, word_rev[end-i:]))
                if word[:i] == word_rev[end-i:] and word_rev[:end-i] in words:
                    palingrams.append((word_rev[:end-i], word))
    return palingrams


print(*find_palingrams(), sep='\n')
