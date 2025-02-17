def sum_even_odd(num):
  
    even = 0
    odd = 0
    for i in num:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even , odd
  
sum_even_odd([1,2,3,4,5,6])
