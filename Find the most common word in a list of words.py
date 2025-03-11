Find the most common word in a list of words
- Input
    - "apple", "banana", "apple", "orange","banana", "apple" 
- Output
    - apple
-------------------------------------------------------------

def most_common_word(a):
    count={}

    for i in a:
        count[i] = count.get(i,0)+ 1

    most_common = max(count, key=count.get)
    return print(most_common)

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
most_common_word(words)
