Count frequency of each word in a sentence
- Input
    - "apple banana apple orange banana apple" 
- Output
    - 'apple': 3,'banana': 2,'orange': 1 
------------------------------------------------

def count_freq(a):
    count={}

    for i in a:
        count[i] = count.get(i,0)+ 1

    for word, freq in count.items():
        print(f"{word}: {freq}")

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count_freq(words)
