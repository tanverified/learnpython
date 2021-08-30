from pprint import pprint

sentence = "This is common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char_freq = sorted(char_frequency.items(),key=lambda kv:kv[1],reverse=True)

print(sorted_char_freq[0])
