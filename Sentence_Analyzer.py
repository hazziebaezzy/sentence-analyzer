input_sentence = input()
frequency = {}
sum_length = 0
max_length = 0
longest_words = []
sentences = len(input_sentence[0: len (input_sentence)-2].split('.'))
new_string = input_sentence.replace('.', '').replace(',', '').replace("\'", '').replace('(;)', '').replace(':', '').split(' ')

for words in range(len(new_string)):
    if new_string[words] == '':
        new_string.pop(words)

nn_string_len = len(''.join(new_string))

for word in new_string:
    word = word.lower()
    if not (word in frequency):
        frequency[f'{word}'] = 1
    else:
        frequency[f'{word}'] += 1

longestWord, idxx, lwIdx = '', 0, -1

print("Word frequency:")
for words in dict(sorted(frequency.items())):
    print(f"- {words}: {frequency[words]}")
    sum_length += len(words)
    words = words.replace("\'s", '')
    
    if len(longestWord) < len(words):
        longestWord = words
        if lwIdx == -1:
            lwIdx = idxx
    idxx += 1 
    
mean_length = sum_length/len(new_string)

for words in new_string:
    if len(longestWord) == len(words) and (words.lower() not in longest_words):
        longest_words.append(words.lower())
    
print(f"\nLongest word(s) with same length:")
for item in sorted(longest_words):
    print(f"- {item}")
    
print(f"\nIndex {lwIdx} of longest word(s): {longestWord}")
print(f"Average word length: {nn_string_len/len(new_string):.2f}")
print(f"Number of sentences: {sentences}")

