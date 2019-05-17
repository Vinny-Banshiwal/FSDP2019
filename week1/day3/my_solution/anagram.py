word1=list(input("Enter string 1").split())
word2=list(input("enter string 2").split())
list1=[]
for item in word1:
    if item in word2:
        list1.append("true")
    else:
        list1.append("false")


if 'false' in list1:
    print("not anagram")
else:
    print("anagram")