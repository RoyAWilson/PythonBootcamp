'''
Capstone image analysis Problem.
'''

import numpy as np
import cv2


def av_pix(image, circles, size) -> list:
    '''
    To return a brightness value to distinquish between silver and copper coins
    args: image - the image to use
    circles - the already produced circles
    size - the size of square to sample in the centre of each coin

    Variables: av_value - list to hold the brightness values of the coins
    col - float to hold the brightness values to append to the list.
    Returns a list of float values.
    '''
    av_value: list = []
    for coords in circles[0, :]:
        col = np.mean(
            img[coords[1] - size: coords[1] + size, coords[0] + size])
        av_value.append(col)
    return av_value


def get_radius(circles2) -> list:
    '''
    Function to return the radii of the circles
    '''
    # Totor gar circles as arg but have renamed to circles2 as got a warning about redefining variable from outside scope.
    radius: list = []
    for coords in circles2[0, :]:
        radius.append(coords[2])
    return radius


img = cv2.imread('capstone_coins.png', cv2.IMREAD_GRAYSCALE)
original_image = cv2.imread('capstone_coins.png', 0)
img = cv2.GaussianBlur(img, (5, 5), 1)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 160,
                           120, param1=50, param2=27, minRadius=60, maxRadius=120)
circles: int = np.uint16(np.around(circles))
count: int = 1
# Dtaw the outer circle:
for i in circles[0, :]:
    cv2.circle(original_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the centre of the circle
    cv2.circle(original_image, (i[0], i[1]), 2, (0, 0, 255), 3)
    # cv2.putText(original_image, str(count),
    #          (i[0], i[1]), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)
    count += 1

# Attempt to classify the coins using radii and brightness

# set up an empty list to hold the values.
values: list = []
radii = get_radius(circles)
bright_values = av_pix(img, circles, 20)

for a, b in zip(bright_values, radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b < 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)
print(values)

# Put the values onto the image file.

count_2 = 0
for i in circles[0, :]:
    cv2.putText(original_image, str(
        values[count_2]) + 'p', (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    count_2 += 1
cv2.putText(original_image, 'Estimated Total Value: ' +
            str(sum(values))+'p', (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)
cv2.imshow('Detected Coins', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#
# print(radii)

#
# print(bright_values)
# print(circles)
# cv2.imshow('Detected Coins', original_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Had nothing but trouble getting opencv to install and reading the doucmentation not making much sense, have never tried image
# manipulation before.  Might come back to the 50p problem when I have more time to read thoroughly through the documentation.
# and work out why I am getting an error every time I try to mark the polygon on the picture.  Something about the arc values all needing
# to be integers?  Sure they are were all integers when I printed them.
