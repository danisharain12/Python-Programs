a=input().lower()
vowel=0
consonents=0

for i in a:
    if i in 'aeiou':
        vowel = vowel + 1
    else:
        consonents = consonents + 1 
print('The numbers of vowels is',vowel,'The numbers of consonents is',consonents)  
