import random


items = ["rusty sword", "silver coin", "ancient scroll", "healing potion"]
def forest_event(name, found_item):
    print(f"{name} found a {found_item} lying in the leaves...")
    
def damage():
    return random.randint(5, 15)  # Random damage between 5 and 15

def get_random_item():
    return random.choice(items)

# Initialize
user_name = input("Enter your name: ")
rou_nd=0
player = {
    "name": user_name,
    "health": 100,
    "inventory": [],
    "gold": 0
}



while player["health"] > 0:
    rou_nd += 1
    print(f"--- {rou_nd} ---")
    
    
    # Random item
    user_found_item = get_random_item()
    player["inventory"].append(user_found_item)
    forest_event(user_name, user_found_item)
    
    # Random event
    roll = random.randint(1, 3)

    if roll == 1:
        print("A wild goblin appears!")
        player["health"] -= 20
    elif roll == 2:
        print("You find a bag of gold!")
        player["gold"] += 50  # player finds gold
    else:
        print("You rest under a tree and regain energy.")
        player["health"] += damage()
        player["health"] = min(player["health"], 100)
        
        
        
    if player["health"] < 50 and player["gold"] >= 50:
        print("You feel rich, but fragile. Seek balance!")

    print(f"{player['name']}'s current health is {player['health']}")
    
print(f"\n{player['name']}'s inventory: {player['inventory']}")
print(player)


print(f"Game over. {player['name']} survived {rou_nd} rounds.")