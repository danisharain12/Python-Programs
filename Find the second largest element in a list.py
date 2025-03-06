Find the second largest element in a list
- Output
- Enter numbers: 10 20 4 45 99 99 33
- Second largest number is: 45
------------------------------------------

def second_largest_num(num):

    num = sorted(set(num))  
    if len(num) < 2:
        return "No second largest number"
    return num[-2]  

number = [10, 20, 4, 45, 99, 99, 33]
second_largest = second_largest_num(number)
print(f"Second largest number is: {second_largest}")
