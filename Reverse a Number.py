## Write a Python function to reverse the digits of an integer.
- Example:
- reverse_number(1234) → 4321
- reverse_number(-5678) → -8765

def reverse_number(r):

    r = list(str(r))
    r.reverse()
    return int(''.join(r))


print(reverse_number(1234))
