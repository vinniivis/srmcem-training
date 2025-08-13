def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
text = "Hi my name is Vineet Vishwakarma"
print(longest_word(text))
