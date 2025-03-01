Count occurrences of a digit in a number
Input:
    - Enter a number: 1123581321
    - Enter the digit to count: 1
Output:
    - The digit 1 appears 4 times in the number 1123581321.
------------------------------------------------------------

def count_occurrence():
    num=int(input("Enter a number"))
    digit = int(input('Enter a digit'))
    count=0

    num = str(num)
    for i in num:
        if i == str(digit):
            count+=1
           
    print(f"The digit {digit} appears {count} {'time' if count == 1 else 'times'} in the number {num}.")

count_occurrence()        
