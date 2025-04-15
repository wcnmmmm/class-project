
import time,sys,random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
player = {
    "hp": 100,
    "max_hp": 100,
    "potions": 2
}

game_state = {
    "clues": 0
}

def combat(enemy_name, enemy_hp, enemy_attack):
    slow_print(f"\n[Combat] You are attacked by {enemy_name}!")
    while enemy_hp > 0 and player["hp"] > 0:
        slow_print(f"\nYour HP: {player['hp']} | {enemy_name}'s HP: {enemy_hp}")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Healing Potion (You have: {})".format(player["potions"]))
        action = input("Choose your action (1/2/3): ").strip()

        if action == "1":
            damage = random.randint(20, 30)
            enemy_hp -= damage
            slow_print(f"You strike {enemy_name} and deal {damage} damage!")
        elif action == "2":
            slow_print("You brace yourself for the enemys attack.")
        elif action == "3":
            if player["potions"] > 0:
                heal = random.randint(25, 40)
                player["hp"] = min(player["max_hp"], player["hp"] + heal)
                player["potions"] -= 1
                slow_print(f"You drink a potion and recover {heal} HP!")
            else:
                slow_print("You're out of potions!")
                continue
        else:
            slow_print("Invalid input.")
            continue

        if enemy_hp > 0:
            enemy_dmg = random.randint(enemy_attack - 5, enemy_attack + 5)
            if action == "2":
                enemy_dmg //= 2
                slow_print("Your defense reduces incoming damage!")
            player["hp"] -= enemy_dmg
            slow_print(f"{enemy_name} hits you for {enemy_dmg} damage!")

    if player["hp"] <= 0:
        slow_print("You collapse... the darkness consumes you.")
        slow_print("[BAD ENDING] - Died in Echo Town")
        sys.exit()
    else:
        slow_print(f"You defeated {enemy_name}!")

def chapter_one():
    slow_print("It's late at night, and it's raining heavily. You're driving an old car on an unfamiliar mountain road...")
    time.sleep(1)
    slow_print("Suddenly, the car shuddered—and stalled.")
    time.sleep(1)
    slow_print("You see a rusty road sign not far away: 'Echo Town'.")
    time.sleep(1)
    choice = input("Have you decided to go into town?  yes/no: ").strip().lower()
    if choice == "yes":
        enter_town()
    else:
        slow_print("You chose to stay in the car... Soon after, a sharp scream pierced the night sky. You never left the mountain road.")
        slow_print("【Bad Ending】")

def enter_town():
    slow_print("You walk into town and the rain taps on your back like cold fingers.")
    slow_print("The town was unusually quiet, with only one street lamp still flickering an eerie light.")
    time.sleep(1)
    first_night()

def first_night():
    slow_print("\nYou come to an old hotel, and the front desk owner hands you a key with a blank face.There was a girl cleaning the hall next to me.")
    slow_print("Room 203, don't wander around. When the bell rings, lock the door.")
    input("\n(Press Enter to continue)")
    slow_print("\n12 o'clock midnight, ——dong——dong——")
    time.sleep(1)
    slow_print("You hear footsteps in the hallway")
    choice = input("What are you going to do? (lock door / peek / hide) ").strip().lower()
    if choice =="lock door":
        slow_print("You locked the door. The footsteps stopped outside the door and didn't leave for a long time...")
        slow_print("You survived, at least for tonight.")
        second_day()
    elif choice == "peek":
        slow_print("You quietly opened the door, and a pair of pale eyes were looking at you...")
        slow_print("A hand suddenly reached in - you could never close the door again.")
        slow_print("【Bad Ending -Curious man】")
    elif choice == "hide":
        slow_print("You hid under the bed, holding your breath. The door opened, and footsteps moved back and forth in the room... and finally left.")
        slow_print("You survived, but fear began to creep in.")
        second_day()
    else:
        slow_print("You hesitate... The door slowly opens in front of you. Darkness floods into your world, and you can't do anything.")
        slow_print("【Bad Ending - Hesitation means death")

def second_day():
    slow_print("\nThe next morning, you go downstairs and find that the boss of the hotel front desk yesterday is gone... No one remembers him.")
    slow_print("You are the only one who still remembers those eyes。") 

def chapter_two():
    slow_print("\n[Chapter Two: The Fog of Clues]")
    slow_print("Morning. But there is no sun—only thick fog and silence.")
    slow_print("Determined, you leave the inn and try to leave the town and find car")
    slow_print("The town is shrouded in perennial fog, and you feel uncomfortable walking in the fog.")
    choice=input("what are you going to do?*(go back to town, still walk in the fog )")
    if choice== "go back to town":
        slow_print("You successfully left the fog, and the looming figures in the fog made you feel lucky to have left the fog. ")
        back_town()
    elif choice=="still walk in the fog":
        slow_print("You slowly get lost in the fog, and like those natives, you stay in this town forever.")
        slow_print("【Bad Ending - Man in the Mist】")
    else:
        slow_print("You hesitated, and because you stayed in the fog for too long, you were trapped in the fog and could never get out. ")
        slow_print("【Bad Ending - Man in the Mist】")
    
    def back_town():
       slow_print("you have to leave the town, your wife and children are waiting for you in home")
       slow_print("After you back to hotile")
       slow_print("You notice...")
       slow_print(" - Broken windows with blood trails.")
       slow_print(" - Strange symbols scrawled on the walls.")
       slow_print(" - A torn note in the gutter: When the bell tolls, they awaken." )
       game_state["clues"] += 1
       slow_print("[Clue Found +1]")

       slow_print("\nYou hear a growl. A mutated dog leaps from the shadows!")
       combat("Mutated Hound", enemy_hp=40, enemy_attack=15)

       slow_print("It drops a piece of parchment before vanishing into the mist.")
       slow_print("It reads: They return... for the guilty... when midnight falls.")
       game_state["clues"] += 1
       slow_print("[Clue Found +1]")

       choice = input("Do you go to the abandoned 'Church' or the haunted 'Mansion'? ").strip().lower()
       if choice == "church":
        church()
       elif choice == "mansion":
        mansion()
       else:
        slow_print("You wander aimlessly and lose precious time. The mist thickens...")
        sys.exit()

def church():
    slow_print("\n[Abandoned Church]")
    slow_print("You push open the heavy doors. Inside, ruined pews and shattered glass.")
    slow_print("Behind the altar, a stone tablet etched with grotesque sigils reads:")
    slow_print("Darkness stirs at the bells final chime. The town remembers its dead.’")
    game_state["clues"] += 1
    slow_print("[Clue Found +1]")
    input("\n(Press Enter to continue)")

def mansion():
    slow_print("\n[Haunted Mansion]")
    slow_print("The door creaks open into damp rot and silence.")
    slow_print("A portrait stares down from above a fireplace—its eyes lifelike and hollow.")
    slow_print("Behind it, a scrap of paper: The guilty walk among us still.")
    game_state["clues"] += 1
    slow_print("[Clue Found +1]")
    input("\n(Press Enter to continue)")

def chapter_three():
    slow_print("\n[Chapter Three: Awakening the Dead]")
    slow_print("The bell tolls—midnight.")
    slow_print("Echoes pulse through the ground as you follow clues to the town’s ancient bell tower.")
    slow_print("Inside, the air is thick with dread. Bloodstained sigils pulse on the walls.")
    slow_print("A hooded figure emerges from the dark—a cursed guardian!")
    combat("Cursed Sentinel", enemy_hp=80, enemy_attack=25)

    slow_print("The guardian falls. A strange key drops from its cloak.")
    slow_print("It reads: Tower Core—the heart of the curse.")
    input("\n(Press Enter to continue)")
    final_decision()

def final_decision():
    slow_print("\n[Final Choice]")
    slow_print("Atop the tower, you face the Heart of the Bell—a grotesque, pulsing relic.")
    slow_print("You must choose:")
    print("1. Destroy it and end the curse. [Type: destroy]")
    print("2. Sacrifice yourself to seal it. [Type: sacrifice]")
    print("3. Use your clues to break the spell. [Type: uncover]")

    choice = input("Your choice: ").strip().lower()

    if choice == "destroy":
        slow_print("You smash the relic. The tower collapses, and the curse fades into the night.")
        slow_print("[TRUE ENDING] - Curse Broken")
    elif choice == "sacrifice":
        slow_print("You kneel before the relic and offer your blood. The curse is sealed once more.")
        slow_print("[HERO ENDING] - Silent Savior")
    elif choice == "uncover":
        slow_print("You arrange the clues, unlocking the truth. The souls are freed with understanding.")
        slow_print("[SECRET ENDING] - Redemption")
    else:
        slow_print("You hesitate. The relic devours your soul.")
        slow_print("[BAD ENDING] - Lost Forever")
    sys.exit()

def start_game():
    slow_print("Welcome to Echo Town: Shadows Return...", 0.06)
    chapter_one()
    chapter_two()
    chapter_three()

if __name__ == "__main__":
    start_game()
chapter_one()