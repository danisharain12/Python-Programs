**Print Fibonacci sequence up to N terms**

- Input: N = 6  
- Output: 0 1 1 2 3 5
------------------------------------------------

def fibonacci_sequence():

    n = int(input('Enter a number'))

    a = 0
    b = 1

    for i in range(n):
        print(a , end='')
        a, b = b, a + b

fibonacci_sequence()
