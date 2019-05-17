

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

s=list(map(lambda item:random.choice(code_names),names))
print(list(s))