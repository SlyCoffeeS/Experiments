import math

rectangle_length = input('Whats the length of the rectangle?')
rectangle_width = input('how about the width?')

length = float(rectangle_length)
width = float(rectangle_width)

perimetere = 2 * (length + width)
area = length * width


print(f"the area is:", perimetere, "perimitere is:", area) 