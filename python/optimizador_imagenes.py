from PIL import Image

frases = ["Play board game","bike","hike","run","exercise","watch TV","read","go to the movies","listen to music","Play video games"]

for i,value in enumerate(frases):
    img = Image.open(f'photos/{value}.jpg')
    img = img.resize((300,300),Image.LANCZOS)
    #img.save(f'{name}-1.jpg', optimize=True, quality=100)
    img.save(f'new/{value}.webp', optimize=True, quality=30) #60(10kB) - 70(12KB) - 80(15KB)