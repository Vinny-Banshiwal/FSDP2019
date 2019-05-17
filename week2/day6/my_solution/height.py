
from functools import reduce   
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0    
    
height_psnt=list(filter(lambda x:"height" in x,people))
print(height_psnt)

height_count=len(height_psnt)
if height_count>0:
    height_total=reduce(lambda a,x:a['height']+x['height'],height_psnt)
    avg=height_total/height_count
print("average",avg)
        
    
    
    
