# === Zombie Decision Game - FINAL Version with death_count FIXED ===

# --- GLOBAL VARIABLES ---
death_count = 0  # MUST be at the top so it's available to all functions

# Inventory dictionary to track items
inventory = {
    "food": 1,
    "first_aid": 1,
    "companion": False,
    "map": False
}

#  GAME START
def start_adventure():
    print("You wake up alone in your apartment. It's eerily quiet.")
    print("Screams echo outside and the TV flashes: 'Infection outbreak. Stay indoors.'")
    first_choice()

# FIRST DECISION: Stay or Leave
def first_choice():
    print("\nDo you:")
    print("1. Barricade yourself inside (type 'shelter')")
    print("2. Pack a bag and leave (type 'move')")
    choice = input("> ").lower()
    if choice == "shelter":
        shelter_path()
    elif choice == "move":
        move_path()
    else:
        print("Invalid input. Try again.")
        first_choice()

# SHELTER PATH
def shelter_path():
    print("\nYou barricade the door. Supplies are low. You hear a knock at night.")
    print("Do you:")
    print("1. Open the door (type 'open')")
    print("2. Stay silent (type 'hide')")
    choice = input("> ").lower()

    if choice == "open":
        print("\nYou open the door. It's a wounded woman. You let her in.")
        print("She turns during the night. You never wake up.")
        print("BAD END — Trust can be fatal.")
        death()

    elif choice == "hide":
        inventory["food"] -= 1
        if inventory["food"] < 1:
            print("You run out of food and die silently.")
            print("BAD END — Quiet death.")
            death()
        else:
            print("You have one meal left. Time to move.")
            safe_zone_or_city()
    else:
        print("Invalid input. Try again.")
        shelter_path()

# MOVE PATH
def move_path():
    print("\nYou exit through the fire escape. Zombies chase a barking dog.")
    print("Do you:")
    print("1. Help the dog (type 'help')")
    print("2. Use distraction and sneak away (type 'sneak')")
    print("3. Call out for survivors (type 'shout')")
    choice = input("> ").lower()

    if choice == "help":
        print("You shout to save the dog, but zombies come for you instead.")
        print("BAD END — Heroism is overrated.")
        death()

    elif choice == "sneak":
        print("You slip away while the zombies are distracted.")
        safe_zone_or_city()

    elif choice == "shout":
        print("You shout. Zombies find you immediately.")
        print("BAD END — Sound is suicide.")
        death()
    else:
        print("Invalid input. Try again.")
        move_path()

# SAFE ZONE OR CITY EXPLORE
def safe_zone_or_city():
    print("\nWhat now?")
    print("1. Go to a safe zone (type 'safe')")
    print("2. Explore the city (type 'city')")
    choice = input("> ").lower()
    if choice == "safe":
        safe_zone_path()
    elif choice == "city":
        city_explore_path()
    else:
        print("Invalid input. Try again.")
        safe_zone_or_city()

# SAFE ZONE PATH
def safe_zone_path():
    print("\nYou begin your journey toward the mountains.")
    if inventory["food"] < 1:
        print("You collapse from hunger.")
        print("BAD END — Starved on the road.")
        death()
        return

    inventory["food"] -= 1

    if inventory["companion"] and not inventory["map"]:
        print("The dog runs ahead. You follow into an ambush.")
        print("BAD END — Trust misplaced.")
        death()
        return

    print("You reach a cabin. It’s quiet. Possibly safe.")
    print("THE END — Peace is temporary.")
    restart_game()

# CITY EXPLORE PATH
def city_explore_path():
    print("\nYou see a pharmacy, alley, and metro.")
    print("Where do you go?")
    print("1. Pharmacy (type 'pharmacy')")
    print("2. Alley (type 'alley')")
    print("3. Metro (type 'metro')")
    choice = input("> ").lower()

    if choice == "pharmacy":
        if inventory["first_aid"] < 1:
            print("Tripwire! A trap goes off.")
            print("BAD END — Booby-trapped.")
            death()
        else:
            inventory["food"] += 2
            inventory["first_aid"] += 1
            end_city_path()

    elif choice == "alley":
        print("You find a wounded man.")
        if inventory["first_aid"] > 0:
            inventory["first_aid"] -= 1
            print("He warns you: Safe zone might be a trap.")
        end_city_path()

    elif choice == "metro":
        print("Darkness. Screams. Something grabs you.")
        print("BAD END — Curiosity killed the survivor.")
        death()
    else:
        print("Invalid input. Try again.")
        city_explore_path()

# NEUTRAL END
def end_city_path():
    print("\nYou escape the city via underground path.")
    print("You find a silent field. You rest.")
    print("THE END — Silence is survival.")
    restart_game()

# DEATH HANDLER
def death():
    global death_count  # ← This line ensures we can modify the global variable
    death_count += 1
    print(f"\nYou have died. Total deaths: {death_count}")
    restart_game()

# RESTART PROMPT
def restart_game():
    choice = input("\nPlay again? (yes/no): ").lower()
    if choice == "yes":
        # Reset inventory
        inventory["food"] = 1
        inventory["first_aid"] = 1
        inventory["companion"] = False
        inventory["map"] = False
        print("\nRestarting...\n")
        start_adventure()
    elif choice == "no":
        print(f"\nThanks for playing. You died {death_count} time(s). Stay safe.")
    else:
        print("Invalid input. Try again.")
        restart_game()

# GAME LAUNCH
start_adventure()
