number_of_lines=0
number_of_words=0

with open("james_joyce_ulysses.txt","rt") as fp:
    for number_of_lines, line in enumerate(open("james_joyce_ulysses.txt","rt"), 1):
        number_of_words += len(line.split())
        