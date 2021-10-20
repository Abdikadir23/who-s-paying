#### WHO'S PAYING?? ####

import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

## Less code ##
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meals today!!")

# more code #

num_item = len(names)

random_num = random.randint(0, num_item -1)
person_who_will_pay = names[random_num]

print(f"{person_who_will_pay} is going to buy the meals today!!")
