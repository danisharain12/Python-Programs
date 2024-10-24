num=int(input("Enter a number"))

for i in range(1,num+1,2):
    for j in range(1,i+1,2):
        print(j,end='')
    for k in range(i-2,0,-2):
        print(k,end='')
    print()
