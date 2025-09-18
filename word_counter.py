para = input("Enter the paragraph: ")

paragraph = para.split(" ")

words_counter = {}

for word in paragraph:
    if word not in words_counter.keys():
        words_counter[word] = 0
    words_counter[word] += 1

top_three_word_counts = sorted(words_counter.values(), reverse=True)[:3]

for word, count in words_counter.items():
    if count in top_three_word_counts:
        print(word)
