
import os
from PIL import Image

from pillow_heif import register_heif_opener
register_heif_opener()


count = 0

#insert your path here:
path=''


for root, dirs, files in os.walk(path):
    for f in files:
        if f.endswith('.HEIC'):
            count += 1

total=count
count=0

for root, dirs, files in os.walk(path):
    for f in files:
               
        if f.endswith('.HEIC'):
            
            im = Image.open(os.path.join(root, f))
            f_jpg = f[:-5] + '.jpg'   # change .heic to .jpg
            im.save(os.path.join(root, f_jpg))
            count += 1
            print(f'{count} of {total} pictures converted.')

print(f'Done')
