from tkinter import W
from PIL import Image
import glob
import os

file_path = r"C:\Users\umut8\Desktop\video_py\images"
images = []
  
for filename in glob.glob(r'C:\Users\umut8\Desktop\video_py\images\*.png'):
    try:
        im=Image.open(filename)
        images.append(im)
    except:
        print("error")


image_path = "C:\\Users\\umut8\\Desktop\\video_py\\saved"
l = len(images)
print (l)

for i in range (l):

    im = images[i]
    width, height = im.size

    title = str(i)
    final_filepath = os.path.join(image_path, title + 'im111' + ".png")
    final_filepath1 = os.path.join(image_path, title + 'im222' + ".png")
    final_filepath2 = os.path.join(image_path, title + 'im333' + ".png")
    final_filepath3 = os.path.join(image_path, title + 'im444' + ".png")


    for i in range (4): 
        if i == 0:

            left = 1
            top = height / height
            right = width / 2
            bottom = height / 2
            
            im1 = im.crop((left, top, right, bottom))
        elif i == 1:

            left = 1
            top = height /2
            right = width / 2
            bottom = height
        
            im2 = im.crop((left, top, right, bottom))
        elif i == 2:

            left = width / 2
            top = height / height
            right = width
            bottom = height / 2
            
            im3 = im.crop((left, top, right, bottom))
        elif i == 3:

            left = width / 2
            top = height / 2
            right = width
            bottom = height
            
            im4 = im.crop((left, top, right, bottom))
            
    im1.save(final_filepath)
    im2.save(final_filepath1)
    im3.save(final_filepath2)
    im4.save(final_filepath3)
