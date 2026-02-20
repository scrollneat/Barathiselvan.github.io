import random
friends = ["Micheal", "Vikas", "Pandi", "Balaji", "Varun"]

# 1st Choice
print(random.choice(friends))
# 2nd choice
random_id = random.randint(0,4)
print(friends[random_id])
