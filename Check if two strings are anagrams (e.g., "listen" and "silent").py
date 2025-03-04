Check if two strings are anagrams (e.g., "listen" and "silent")

- Enter first string: listen  
- Enter second string: silent  
- The strings are anagrams.
--------------------------------------------------------------------

  def anagrams():
    a = input('Enter first string').lower()
    b = input('Enter second string').lower()

    if sorted(a) == sorted(b):
        print(f"{a} and {b} are anagrams")
    else:
        print(f"{a} and {b} are not anagrams")

anagrams()
