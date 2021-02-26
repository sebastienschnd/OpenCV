# import the necessary packages
import numpy as np
import argparse
import cv2

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# convert the image to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


boundaries = [
	([110, 50, 50], [130, 255, 255])
]

#loop over the boundaries
for (lower, upper) in boundaries:
    # create Numpy array from the boundaries
    lower = np.array(lower)
    upper = np.array(upper)

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(hsv, lower, upper)

    # show the image mask
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
    cv2.destroyWindow("mask")

    # apply mask on image
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)


