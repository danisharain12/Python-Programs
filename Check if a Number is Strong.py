**Check if a Number is Strong**

**A strong number is a number where the sum of the factorial of its digits is equal to the number itself.**

✅ Example:
- 145 → 1!+4!+5!=1+24+120=145 ✅ Strong Number
- 123 → 1!+2!+3!=1+2+6=9 ❌ Not a Strong Number
---------------------------------------------------------------------------------------------------------------

def strong_num():
    num = int(input("Enter a number"))
    original_num = num 
    sum_fact = 0  

    while num > 0:
        digit = num % 10  
        num = num // 10  

        
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        
        sum_fact += fact  


    if sum_fact == original_num:
        print(f"{original_num} is a Strong Number")
    else:
        print(f"{original_num} is NOT a Strong Number")

strong_num()
