import os
#os.listdir()
from PIL import Image
file=os.listdir(".")
for files in file:
     if files.endswith('.jpg'):
         im=Image.open(files) 
         fn, text = os.path.split(files)
         #i.save('pngs/{}.png'.format(file))
 