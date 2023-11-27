'''
To set filters on an image; warm and cold filters
using cv2 and numpy for image manipulation.
'''

import numpy as np
import cv2
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# Set the path to the image file
PATH = 'cricket.JPG'

# Read the image in

img = mpimg.imread(PATH)

# Set image size and show the image, then close the plot.  Weird plt.close() seems to stop the image from opening.
# Previously with graphs closing the plot has been needed if intending to show any other plots.

plt.rcParams['figure.figsize'] = [15, 18]
# plt.imshow(img)

# Define a mapping funciont


def mapping_function(x, y):
    '''
    Funciton maps values and
    spl - var to hold the mapped values
    and interpolate values not in the given ranges and return it.
    '''
    spl = UnivariateSpline(x, y)
    return spl(range(256))

# Define the warm filter for the image


def apply_warm(image):
    '''
    To apply warm filter to image
    by mapping values given for x in mapping function by given amount
    incresase increases reds and decrease decreases blues.
    Values not mentioned in the lists will be increased or decreased
    automatically by an equivalent amount handled by the image processing package
    args: iamge - an image file to work on
    vars: increase - a set of lists containing the value changes to make and the value to increase to
    decrease - as above except the decrement value in second list
    red, greem, blue - variables into which to split the colour information of the image.
    '''

    increase = mapping_function([0, 64, 128, 192, 256], [0, 70, 140, 210, 256])
    decrease = mapping_function([0, 64, 128, 192, 256], [0, 40, 90, 150, 256])
    red, green, blue = cv2.split(image)
    red = cv2.LUT(red, increase).astype(np.uint8)
    blue = cv2.LUT(blue, decrease).astype(np.uint8)
    image = cv2.merge((red, green, blue))
    return image

# Function to apply cold filter by reducing reds and increasing blues


def apply_cold(image):
    '''
    To apply a decrease in the blues
    to effect a cold image filter
    decreases reds and increases the blues and return the image.
    Values not mentioned in the lists will be increased or decreased
    automatically by an equivalent amount handled by the image processing package
    args: iamge - an image file to work on
    vars: increase - a set of lists containing the value changes to make and the value to increase to
    decrease - as above except the decrement value in second list
    red, greem, blue - variables into which to split the colour values of the image.
    '''
    increase = mapping_function([0, 64, 128, 192, 256], [0, 70, 140, 210, 256])
    decrease = mapping_function([0, 64, 128, 192, 256], [0, 40, 90, 150, 256])
    red, green, blue = cv2.split(image)
    red = cv2.LUT(red, decrease).astype(np.uint8)
    blue = cv2.LUT(blue, increase).astype(np.uint8)
    image = cv2.merge((red, green, blue))
    return image


# new_image = apply_cold(img)
# plt.imshow(new_image)
# plt.savefig('img_cold.jpg')

# Now working can't see where I mistyped in the previous file.
