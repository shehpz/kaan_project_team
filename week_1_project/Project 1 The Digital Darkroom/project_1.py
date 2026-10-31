import cv2
import numpy as np


#We used the provided websites to understand how the methods work and to determine which methods are better suited for the questions we were asked.
#https://docs.opencv.org/4.13.0/db/deb/tutorial_display_image.html
#https://www.geeksforgeeks.org/python/warm-and-cool-image-effects-in-opencv/
#https://www.geeksforgeeks.org/python/python-grayscaling-of-images-using-opencv/
#https://docs.opencv.org/4.13.0/d3/df2/tutorial_py_basic_ops.html
#https://docs.opencv.org/4.13.0/d2/d96/tutorial_py_table_of_contents_imgproc.html

# Here we are getting file path by user input.
# With cv2.imread, we read img path. 
path = input("Please enter file path: ")

image = cv2.imread(path)

if image is None:
    print("Error by file path.")
    

# cv2.imshow show image on display with orijinal size img. 
cv2.imshow("Image", image)
cv2.waitKey(0)

#we can see image info by shape method.
#we define here.
height, width, color_channels = image.shape

print("------ Image Info ------")
print(f"Height: {height}")
print(f"Width: {width}")
print(f"Color Channels: {color_channels}")


#Here we define BGR color system one by one color.
blue_channel, green_channel, red_channel = cv2.split(image)


cv2.imshow("Blue Channel", blue_channel)
cv2.waitKey(0)
cv2.imshow("Green Channel", green_channel)
cv2.waitKey(0)
cv2.imshow("Red Channel", red_channel)
cv2.waitKey(0)

#With cv.merg we can merge color system we want. for example B,G,R or R,G,B.

new_merge_image= cv2.merge((red_channel,green_channel,blue_channel))

cv2.imshow("Merge Image", new_merge_image)
cv2.waitKey(0)



# Here we are getting percent by user and we use this value to cropping to image.

perce = int(input("what percentage to resize by: "))

new_crop_image = image[0:height- int(height*perce/100),0:width- int(width*perce/100) ]

cv2.imshow("Croped Image", new_crop_image)
cv2.waitKey(0)


# Here, we resize the cropped image to make it larger again.

new_resized_image = cv2.resize(new_crop_image,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Resized Image", new_resized_image)

cv2.waitKey(0)



# Here we change color to gray tone with .cvtColor method.
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale image",grayscale_image)
cv2.waitKey(0)



#Here we add warm and vintage filter with use np.full method. 
warm_bg = np.full((height, width, 3), (0, 180, 255), dtype=np.uint8)
warm = cv2.addWeighted(image, 0.7, warm_bg, 0.3, 0)
cv2.imshow("Warm Image", warm)
cv2.waitKey(0)

vintage_bg = np.full((height, width, 3), (60, 105, 150), dtype=np.uint8)
vintage = cv2.addWeighted(image, 0.75, vintage_bg, 0.25, 0)
cv2.imshow("vintage Image", vintage)
cv2.waitKey(0) 


