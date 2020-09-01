"""
Python assignment 4
Filter long words
"""
def filter_long_words(lst,n):
    l=len(lst)
    new_lst=[]
    if l>n:
        for i in range(l-n+1, l):
            if n==l:
                break
            new_lst.append(lst[i])
          
        print("The filtered words are :\n", new_lst)
    else:
        print("The given list is not enough long to be printed")   
        
n= int(input("Enter the number : "))    
lst = []
lst =[item for item in input("Enter the list items : \n").split()]          
filter_long_words(lst,n)          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        

