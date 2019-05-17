string=input("Enter a string").lower()

def translate(string):
    vowels=['a','e','i','o','u']
    output=[]
    for element in string:
        if (element not in vowels):
            element=element+'o'+element
            output.append(element)
        else:
            element=element
            output.append(element)
    print(output)
translate(string)
            
            