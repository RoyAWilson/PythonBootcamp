# To find the area of a circle given radius input

# Area = piR^2
import math

p = math.pi

rad = float(input('What is the radius of the circle? \t >> '))

area = p*(rad**2)

print(f'The area of circle radius {rad} is {
      round(area, 2)}, rounded to 2 decimal places')
