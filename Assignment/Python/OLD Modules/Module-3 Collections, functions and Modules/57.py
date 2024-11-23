# 57. How will you randomizes the items of a list in place? 


# To randomize (shuffle) the items of a list in place, you can use the 
# random.shuffle() function from the random module. This modifies the 
# original list, shuffling its elements randomly.

import random


my_list = [1, 2, 3, 4, 5]

# Shuffling the list in place
random.shuffle(my_list)

print(my_list)



my_list = [1, 2, 3, 4, 5]
# if i set the seed everytime i got same output
random.seed(10)

random.shuffle(my_list)

print(my_list)
