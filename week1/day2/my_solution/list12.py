state_name = ['Alabama','California','Oklahoma','Florida']
vowels=['a','e','i','o','u']
output=[]

for item in state_name:
    st_nm=list(item.lower())
    for element in vowels:
            while element in st_nm:
                st_nm.remove(element)
    output.append("".join(st_nm))
              
        
        
print(output)