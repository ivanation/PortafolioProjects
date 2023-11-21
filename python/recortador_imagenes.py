import sys, os
from PIL import Image

#grab first argument
image_folder = sys.argv[1]
output_older = sys.argv[2]

#check if new/ exist or create
if not os.path.exists(output_older):
    os.makedirs(output_older)

print(image_folder, output_older)



# loop through pokedex, convert img to png save the new folder
for filename in os.listdir(image_folder):

    # My image is a 200x374 jpeg that is 102kb large
    img = Image.open(f'{image_folder}{filename}')
    img.size
    
     # downsize the image with an ANTIALIAS filter (gives the highest quality)
    img = img.resize((300,300),Image.ANTIALIAS) 

    # The saved downsized image size is 22.9kb
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_older}{clean_name}.jpg', optimize=True, quality=85)
    print('all done!')
