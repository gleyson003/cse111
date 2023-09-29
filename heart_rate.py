"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input('Please enter your age: '))
range = 220 - age
heart_rate_minimum = int(range * 0.65)
heart_rate_maximum = int(range * 0.85)

print(f'When you exercise to strengthen your heart, you should \nkeep your heart rate between {heart_rate_minimum} and {heart_rate_maximum} beats per minute.')
