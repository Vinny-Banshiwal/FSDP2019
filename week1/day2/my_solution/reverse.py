string=input("string")

def reversal(string):
    out_string=""
    for element in string:
        out_string=element+out_string
    print(out_string)
        
reversal(string)
    