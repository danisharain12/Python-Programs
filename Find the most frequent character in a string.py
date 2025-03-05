Find the most frequent character in a string
- Input: "banana"
- Output: 'a' (since 'a' appears 3 times, which is the most)
------------------------------------------------------------

def most_freq_char():
    a=input('Enter a string:')
    count={}

    for i in a:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    max_char = max(count, key=count.get)  
    print(f"Enter a string: {a}")
    print(f"Most frequent character in a string is: {max_char}")

most_freq_char()
        
