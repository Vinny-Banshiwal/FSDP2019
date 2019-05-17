with open("absentee.txt","wt")as fp:
    while(True):
        user_input=input("Enter name")
        if not user_input:
            break
        else:
            fp.write(user_input+"\n")
            