#Write generator, which generates numbers
# in a given range (from a certain number to a certain number)

#1 chapter
# import random
#
# lower_bound = 90
# upper_bound = 150
#
# random_number = random.randint(lower_bound, upper_bound)
# print("Random number", lower_bound, "to", upper_bound, ":", random_number)

#2 chapter
import random

lower_bound = 90
upper_bound = 150

for i in range(1, 6):
    random_number = random.randint(lower_bound, upper_bound)
    print(f"Number {i}: {random_number}")
