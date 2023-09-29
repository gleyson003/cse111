import math
from datetime import datetime

def tires_informations(width, aspect, diameter, volume, phone=None):
    with open('volumes.txt', "a") as file_volume:
        if phone is None:
            output_string = f'{datetime.now():%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}'
        else:
            output_string = f'{datetime.now():%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {phone}'
        
        print(output_string, file=file_volume)

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter)) / 10000000000
print(f'\nThe approximate volume is {volume:.2f} liters.\n')

buy = input("Do you want to buy tires with the dimensions that you entered? Y / N ")

if buy.upper() == "Y":
    phone_number = input("Enter your phone: ")
    tires_informations(width, aspect, diameter, volume, phone_number)
else:
    tires_informations(width, aspect, diameter, volume)
    
