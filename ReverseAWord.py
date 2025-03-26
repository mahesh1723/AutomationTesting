def reverse_word(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_word("Hello World"))