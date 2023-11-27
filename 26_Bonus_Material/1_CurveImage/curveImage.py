import numpy as np
import cv2
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# read in the picture details
path = 'cricket.JPG'

img = mpimg.imread(path)
plt.rcParams['figure.figsize'] = [18, 15]
# plt.imshow(img)
# plt.close()

# Function to map values.


def mapping_function(x, y):
    '''
    Funciton maps values and
    spl - var to hold the mapped values
    and interpolate values not in the given ranges.
    '''
    spl = UnivariateSpline(x, y)
    return (spl(range(256)))

# Function to add warm filter to image.


def apply_warm(image):
    '''
    To apply warm filter to image
    by mapping values given for x in mappying function by given amount
    incresase increases reds and decrease decreases reds
    '''
    increase = mapping_function([0, 64, 128, 192, 256], [0, 70, 140, 210, 256])
    decrease = mapping_function([0, 64, 128, 192, 256], [0, 40, 90, 150, 256])
    red, green, blue = cv2.split(image)
    red = cv2.LUT(red, increase).astype(np.uint8)
    blue = cv2.LUT(blue, decrease).astype(np.uint8)
    image = cv2.merge((red, green, blue))
    return image


def apply_cool(image):
    '''
    To apply a decrease in the blues
    to effect a cold image filter
    decreases reds and increases the blues
    '''
    increase = mapping_function([0, 64, 128, 192, 256], [0, 70, 140, 210, 256])
    decrease = mapping_function([0, 64, 128, 192, 256], [0, 40, 90, 150, 256])
    red, green, blue = cv2.split(image)
    red = cv2.LUT(red, decrease).astype(np.uint8)
    blue = cv2.LUT(blue, increase).astype(np.uint8)
    image = cv2.merge((red, green, blue))
    return image


new_image = apply_cool(img)
plt.savefig(new_image)
plt.imshow(new_image)
plt.close()
# image_warm = apply_warm(img)
# plt.show(image_warm)
# plt.close(another)
# Shit corrected an error in the code and now it has stopped working completely!  Might be quicker to just
# retype the whole bloody lot of it.
