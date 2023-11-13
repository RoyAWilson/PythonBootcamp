from PIL import Image, ImageFilter, ImageFont
from matplotlib.pyplot import imshow
import PIL

# file_name = 'hillside.jpg'
im = Image.open(r'../_Notes_Resources/13.6_hillside_for_PIL_example.jpg')
# course tutor omitted the dot between im and show
# im.show(im)


print(im.size)
print(im.format_description)
print(im.mode)
crop = (200, 200, 600, 600)
cropped_image = im.crop(crop)
# im.show(cropped_image)
im.save(r'../Output/cropped_im.jpg')

im_resized = im.resize((400, 200))
# im.show(im_resized)
im.save(r'../Output/resize.jpg')

# Greyscale is not working.

grey_scale = im.convert('LA')
# im.show(grey_scale)
im.save(r'../Output/greyscale.jpg')

effect = im.filter(ImageFilter.GaussianBlur(radius=100))
im.show(effect)
im.save(r'../Output/gauzian.jpg')
im.close()

# None of these are working as per the tutorial
