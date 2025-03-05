Remove duplicate characters from a string
- Input: "banana"
- Output: "ban" (Duplicates 'a' and 'n' are removed, keeping only the first occurrence)
----------------------------------------------------------------------------------------

def duplicate_char():
    a=input('Enter a string:')
    b=[]
    c=set()

    for i in a:
        if i not in c:
            b.append(i)
            c.add(i)
    print(f'Enter a string: {a}')
    return ''.join(b)

duplicate_char()
