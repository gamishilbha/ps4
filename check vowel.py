"""
Python assignment 4
Returns True if it is a vowel or False
"""
def vowel(s):
    if s.lower() in 'aeiou':
        return True
    if s.upper() in 'AEIOU':
        return True
    else:
        return False  
lst =[item for item in input("Enter the list of character with string length 1 : \n").split()] 
a=map(vowel, lst)
results=list(a)
print(results)