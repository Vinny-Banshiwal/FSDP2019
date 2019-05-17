
list1=[]
word_count={}
with open("romeo.txt",mode="rt") as file_read:
    line1=file_read.read().split()
    print(line1)
    for word in line1:
    #adding every element as a 'key' and its frequency of occurance
    #as 'value' in the Dict.
        word_count[word]=word_count.get(word,0)+1
    print(word_count)
    
    
    
    
    
    
    
    
    
    
    
    
    
