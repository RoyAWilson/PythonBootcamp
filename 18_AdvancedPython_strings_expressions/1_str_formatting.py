''''
More on strings.  Formatting decimal number in strings
'''

import math

PI: float = math.pi

print(f'Pi = {PI}')
# Below the 'f' after the 3 makes three decimal place not only 3 digits including decimal places
print(f'Pi to three decimal places = {PI:.3f}')
# Below 12.3f 12 controls the padding before the number is displayed and 3f as above
print(f'Pi to three decimal places = {PI:12.3f}')
# Below as above except 0 padded
print(f'Pi to three decimal places = {PI:012.3f}')
# Below adds a plus sign to front of the number doesn't seem to work with the '-' for signing but displays anyhow if no is neg
print(f'Pi to three decimal places = {PI:+.3f}')
print(f'Pi to three decimal places = {PI:-.3f}')
# Below align to left of the padding
print(f'Pi to three decimal places = {PI:<10.3f}')
# Below - Centre to padding
print(f'Pi to three decimal places = {PI:^10.3f}')
# Below add sign and padding but unfortunately the plus is before the padding
print(f'Pi to three decimal places = {PI:=+10.3f}')
