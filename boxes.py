import math

n_items = int(input("Enter the number of items: " ))
items_box = int(input("Enter the number of items per box: "))

n_boxes = n_items / items_box

print(f'For {n_items} items, packing {items_box} items in each box, you will need {math.ceil(n_boxes)} boxes.')