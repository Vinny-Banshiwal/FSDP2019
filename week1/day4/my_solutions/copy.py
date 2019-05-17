#to copy a file
with open("romeo2.txt",mode="rt") as fp:
    with open("copyromeo.txt",mode="wt") as cfp:
        for line in fp:
            cfp.write(line)
