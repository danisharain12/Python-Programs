Find the sum of elements at even and odd indices separately
- Input:
  - [3, 1, 4, 2, 5, 6, 7, 8]
- Output:
  - Sum at even indices: 19
  - Sum at odd indices: 17
------------------------------------------------------------

def sum_even_odd_indices(num):
    even_indices=0
    odd_indices=0

    for i, val in enumerate(num): 
        if i % 2 == 0: 
            even_indices += val
        else:
            odd_indices += val

    return f"Sum at even indices: {even_indices}\nSum at odd indices: {odd_indices}"

nums = [3, 1, 4, 2, 5, 6, 7, 8]
print(sum_even_odd_indices(nums))
