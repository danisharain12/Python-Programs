**Write a Python function to check if a given integer is a palindrome.**
- A palindrome number reads the same forward and backward.
- Example:
✅ is_palindrome(121) → True
✅ is_palindrome(-121) → False (Negative numbers are not palindromes)
✅ is_palindrome(123) → False
- Constraints:
- Do not convert the number into a string.
- Your solution should work for both positive and negative numbers.
---------------------------------------------------------------------------------

def palindrome_number(p):

    if p < 0:
        return False

    original = p
    reversed_number = 0

    while p > 0:
        digit = p % 10
        reversed_number = reversed_number * 10 + digit
        p //= 10

    return original == reversed_number

print(palindrome_number(121))
print(palindrome_number(-121))
print(palindrome_number(232))
