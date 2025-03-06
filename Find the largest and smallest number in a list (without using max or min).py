Find the largest and smallest number in a list (without using max or min)
- Output
- Largest: 422, Smallest: -3
--------------------------------------------------------------------------

def lar_sma_num(num):
    largest=num[0]
    smallest=num[0]

    for i in num:
        if i > largest:
            largest=i
        elif i < smallest:
            smallest=i
    return largest , smallest

numbers = [12,422,53,-3,0,4,33]
largest, smallest = lar_sma_num(numbers)
print(f"Largest number is: {largest}, Smallest number is: {smallest}")
