#importing random class 
import random
#list of fruits
fruits=['mango','banana','grapes','papaya']


letter=random.choice(fruits)

print("Random word choosen=",letter)
letter1=[]
for item in letter:
    letter1.append(item)
    
guess=''
turns=10
guess_word=''
while(turns>0):
    fails=0
    guess=input("characters")        
    guess_word=guess
    for char in letter:
        if char in guess_word:
            print(char)
        else:
            print("_")
            
            fails+=1
            
    if(fails==0):
        print("match")
        break
   