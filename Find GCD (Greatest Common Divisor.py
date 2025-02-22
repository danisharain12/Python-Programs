**Write a function to find the Greatest Common Divisor (GCD) of two numbers without using built-in functions like math.gcd().**
- Example:
- ✅ gcd(48, 18) → 6
- ✅ gcd(101, 103) → 1
---------------------------------------------------------------------------------------------------------------------------------

def gcd(a, b):
    while b != 0:  
        a, b = b, a % b  
    return a  

print(gcd(101,103))  
