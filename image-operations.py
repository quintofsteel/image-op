from __future__ import print_function
import cv2
import numpy as np


image_path = "/home/quint/cvpride.jpg"
image = cv2.imread(image_path)

def translation():
    translationMatrix = np.float32([[1, 0, 50], [0, 1, 20]])

    movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))  # moving the image

    cv2.imshow("Moved Image", movedImage)
    cv2.waitKey(0)

def rotation():
    (h, w) = image.shape[:2]
    centre = (h // 2, w // 2)
    angle = -45
    scale = 1.0

    rotationMatrix = cv2.getRotationMatrix2D(centre, angle, scale)

    rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1], image.shape[0]))

    cv2.imshow("Rotated Image", rotatedImage)
    cv2.waitKey(0)


def flipping():
    flippedHorizontally = cv2.flip(image, -1)  # 1 = horizontally, 0 = vertically, -1 = horizontally then vertically
    cv2.imshow("Flipped Horizontally", flippedHorizontally)
    cv2.waitKey(-1)

print("Which image operation would you to make: ")
print("F/f  ---> Flipping the image")
print("T/t  ---> Translating the image")
print("R/r  ---> Rotating the image")

reply = input()

if (reply.lower() == "f"):
    flipping()
elif (reply.lower() == "t"):
    translation()
elif (reply.lower() == "r"):
    rotation()
else:
    print("Invalid choice.")


    
