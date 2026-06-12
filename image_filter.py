import numpy as np
from PIL import Image
img = Image.open("boat.png")
array= np.array(img)
print(array.shape)
print("Successfully loaded image with shape:", array.shape) 
print("-" * 30)
print("---matrix image filter---")
print("1: invert filter")
print("2: brightness booster")
print("3: grayscale filter")
choice= input("choose a filter(1,2 or 3):")
if choice== "1":
    print("applying invert filter..")
    inverted_array= 255-array
    inverted_img= Image.fromarray(inverted_array.astype(np.uint8))
    inverted_img.save("inverted_boat.png")
    print("inverted image saved successfully!")
elif choice== "2":
    print("applying brightness filter..")
    bright_array=np.clip(array+50,0,255)
    bright_array=Image.fromarray(bright_array.astype(np.uint8))
    bright_array.save("bright_boat.png")
    print("image saved successfully")
elif choice== "3":
    print("applying gray filter")
    gray_array=np.mean(array,axis=2)
    gray_array=Image.fromarray(gray_array.astype(np.uint8))
    gray_array.save("gray_boat.png")
    print("image saved successfully")
else:
    print("invalid choice! please run the script again and choose 1, 2, or 3.")
#cropping the image
cropped_array= array[100:500,200:600]
red_only=array.copy()
red_only[:,:,1]=0                    
red_only[:,:,2]=0
cropped_array=Image.fromarray(cropped_array.astype(np.uint8))
cropped_array.save("red_boat.png")
     









                           