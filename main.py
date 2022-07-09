# Image Libraries Used
from PIL import Image  
import cv2
import numpy as np

image_path = "moavia.jpg"  # Address of Image you want to write in Text File

x_pixels = 160       # Here Write the number of pixels along X-axis for vga
y_pixels = 120       # Here Write the number of pixels along Y-axis for vga
center_x = 1/2      # Here You provide the center to widht for Croping the original image (1/2 indicate at mid)
center_y = 1/3      # (1/3 indiacte take center little above from original Image)
im1 = Image.open(image_path)
w,h = im1.size
print("Previous Size ",w,h)

# Here Croping Image size to integer multiple of 160x120 image
# We take that integer number as k 
if((w//x_pixels)>(h//y_pixels)):
    k = h//y_pixels
else:
    k = w // x_pixels    

if(w == x_pixels):
    if (h == y_pixels):
        im2 = im1
    elif(h > y_pixels):
        im2 = im1.crop((0,h*center_y-(k*y_pixels)/2,x_pixels,h*center_y+(k*y_pixels)/2))
    else:
        print("hight is less than minimum value")
elif (w > x_pixels):
    if (h == y_pixels):
        im2 = im1.crop((w*center_x-(k*x_pixels)/2,y_pixels,w*center_x+(k*x_pixels)/2,0))
    elif(h > y_pixels):
        im2 = im1.crop((w*center_x-(k*x_pixels)/2,h*center_y-(k*y_pixels)/2,w*center_x+(k*x_pixels)/2,h*center_y+(k*y_pixels)/2))
    else:
        print("hight is less than minimum value")
else:
    if (h<y_pixels):
        print("Hight and width are less than minimum")
    else:
        print("Hight is less than minimum")

w,h = im2.size
print("Size After Croping is : \n Width = ",w,"\n Hight = ",h)

# Now image if perfectly integer multiple of 160x120
# Resizing Image to 160x120
im3 = im2.resize((x_pixels,y_pixels))
im1.show()
im2.show()
im3.show()
im3.save("ResizedImage.png")

# using CV2 for colour channel separation
im4 = cv2.imread("ResizedImage.png")
b,g,r = (cv2.split(im4))

file = open("ResizedImage.txt","w") # creating a text file for writing perpose

# Writing Data of Each colour channel in Text File in 8 bit binary each (.zfill(8)) 
for i in range (y_pixels-1):
    for j in range (x_pixels-1):
        a = bin(r[i][j]).replace('0b',"").zfill(8)
        file.write(a)
        a = bin(g[i][j]).replace('0b',"").zfill(8)
        file.write(a)
        a = bin(b[i][j]).replace('0b',"").zfill(8)
        file.write(a)
        file.write("\n")
print("Done...")        


