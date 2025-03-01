Find sum of all even and odd digits in a number
- Input:
    - Enter a number: 248315
- Output:
    - Sum of even digits: 14
    - Sum of odd digits: 9
------------------------------------------------

def sum_even_odd():
    num=int(input('Enter a number'))
    even=0
    odd=0

    num=str(num)
    for i in num:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    print(f"Sum of even digits:{even}")
    print(f"Sum of odd digits:{odd}")

sum_even_odd()    
