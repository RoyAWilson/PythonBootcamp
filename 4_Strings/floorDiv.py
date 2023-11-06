# Floor division:
# 4 people want to order pizza they each want 4 slices, the pizza place
# delivers pizzas in six slices.  What is the minimum number of pizzas they
# need to order?

# fomula would be people x number of slices + 5 // 6
# slices left will be number of pizzas * 6 - total slices required

NUMBERSLICES: int = 4 * 4
needed: int = (NUMBERSLICES + 5) // 6
left: int = needed * 6 - NUMBERSLICES

print(f'The minimum number of pizzas needed is {
      needed}, \n the number of remaining slices is {left}')
