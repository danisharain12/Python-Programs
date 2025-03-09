Find the most frequently occurring element in a list
- Input:
  - [3, 1, 4, 3, 2, 3, 4, 4, 4, 5]
- Output:
  - 4 (occurs 4 times)
-----------------------------------------------------

def most_freq(num):
    count = {}  

    for i in num:
        count[i] = count.get(i, 0) + 1  

    most_frequent_element = max(count, key=count.get)  
    max_count = count[most_frequent_element]  

    return f"{most_frequent_element} (occurs {max_count} times)"

nums = [3, 1, 4, 3, 2, 3, 4, 4, 4, 5]
print(most_freq(nums)) 
