
import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
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
        slow_print("【Bad Ending -chosen one】")
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

