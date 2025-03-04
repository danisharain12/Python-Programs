Reverse a string without using [::-1]
- Enter a string: hello  
- Reversed string: olleh
-------------------------------------

def reverse_string():
    a=list(input('Enter a string'))

    a.reverse()
    print('Reversd string',''.join(a))
    
reverse_string()
