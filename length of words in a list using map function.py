"""
Python assignment 4
function to map the list into length of each word
"""

def lst_word_len(x):
    l=len(x)
    return l
        
lst =[item for item in input("Enter the list items : \n").split()] 
results=map(lst_word_len, lst)
print(list(results))