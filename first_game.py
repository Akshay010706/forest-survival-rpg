import random 

items = ["rusty sword", "silver coin", "ancient scroll", "healing potion"] 
def forest_event(name,found_item):
     print(f"{name} found a {found_item} lying in the leaves...")

health = 100
user_name = input("Enter your name:")
user_found_item = random.choice(items)

forest_event(user_name,user_found_item)

roll = random.randint(1, 3)

if roll == 1:
    print("A wild goblin appears!")
    health -= 20  # player loses 20 HP
elif roll == 2:
    print("You find a bag of gold!")  # no health change
else:
    print("You rest under a tree and regain energy.")
    health += 10  # player heals
    health = min(health, 100)

print(f"{user_name}'s current health is {health}") 