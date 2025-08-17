import random


items = ["rusty sword", "silver coin", "ancient scroll", "healing potion"]
inventory = []
def forest_event(name, found_item):
    print(f"{name} found a {found_item} lying in the leaves...")

# Initialize
user_name = input("Enter your name: ")
health = 100


# Run 3 rounds
for round in range(3):
    print(f"\n--- Round {round + 1} ---")
    
    # Random item
    user_found_item = random.choice(items)
    inventory.append(user_found_item)
    forest_event(user_name, user_found_item)
    
    # Random event
    roll = random.randint(1, 3)

    if roll == 1:
        print("A wild goblin appears!")
        health -= 20
    elif roll == 2:
        print("You find a bag of gold!")
    else:
        print("You rest under a tree and regain energy.")
        health += 10
        health = min(health, 100)

    print(f"{user_name}'s current health is {health}")
    
print(f"\n{user_name}'s inventory: {inventory}")


