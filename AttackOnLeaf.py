import time  # time package imported

print("MADARA UCHIHA HAS REAPPEARED IN THE HIDDEN LEAF VILLAGE! YOU   MUST DEFEAT HIM!")
print("----------------------------------------------------\n")
time.sleep(1.2)  # time lapse between next text appearing
player_class = ""
enemy = "Madara Uchiha"

while player_class != "Naruto" or player_class != "Sasuke":  # player class defined
    print("Which ninja do you wish to be?\n\nPlease choose either 'Naruto' or 'Sasuke':")
    player_class = input()
    player_class = player_class.lower()  # returns the lowercased string from the given string
    if player_class == "naruto":
        print()
        print(
            "You are Naruto Uzumaki. The infamous 'hyperactive knucklehead  ninja'. You possess the great power of the Nine Tails.")
        print(
            "Madara has returned to seek vengeance against the Hidden Leaf Village. Using the power of the Nine Tails, you must stop him!")
        print()
        player_class = "naruto"
    elif player_class == "sasuke":
        print()
        print(
            "You are Sasuke Uchiha, lone survivor of the Uchiha clan. Using your powerful sharingan, you must stop Madara from destroying the leaf village!")
        print()
        player_class = "sasuke"
    else:  # Player must select one the choices provided
        print("\nAll other ninjas are unavailable.Please choose either 'Naruto' or 'Sasuke' to proceed.\n")
        print("\n---------------------------------------------------\n")
        continue
    break  # terminates current loop

    # This portion is seperate from loop
    # Defines character attack/health

attack = "Attack"
defend = "Defend"
attack_button = "A"  # Assigns attack button for users
defend_button = "D"  # Assigns defence button for users
dmg = 60
full_health = 250
health = full_health
chakra = 100
super_smash = dmg * 1.7
full_enemy_health = 300
enemy_health = full_enemy_health
firebolt_damage = 50
dfd = firebolt_damage * 0.5  # Using defend halves damage output
dfd = int(dfd)
battle_choice_made = False
current_health = 'print(f"Health = {health}/{full_health}")'
current_enemy_health = 'print(f"Enemy Health = {enemy_health}/{full_enemy_health}")'
under_attack_message = 'print(f"{enemy} charges his chakra and unleashes a fireball jutsu, striking you down.")'

print(
    f"You have arrived to battle {enemy}. Prepare to leave everything on the line or the village will be destroyed...")
print()

while health > 0 or enemy_health > 0:

    print("---------------------------------------------------")
    print("~                                                        ~")
    print(f"#  {attack} or {defend}                                   #")
    print("~                                                        ~")
    print("# What would you like to do?                             #")
    print(f"# ~ '{attack_button}' for attack or '{defend_button}' for defend:                      ~")
    battle_choice = input("# ")
    battle_choice = battle_choice.lower()
    battle_choice_made = True
    print("---------------------------------------------------")

    while battle_choice_made == True:
        if battle_choice == "d":
            print("\nYou will receive 50% less damage the next time you are attacked.\n")
            last_choice = defend_button
            if enemy_health > 0:
                exec(under_attack_message)
                print("The damage has been reduced due to your increaseed defence!\n")
                health = health - dfd
                exec(current_health)
                exec(current_enemy_health)
                print()
            else:
                exec(current_health)
                exec(current_enemy_health)
                print()
        elif battle_choice == "a":
            enemy_health = enemy_health - dmg
            print(f"\nYou unleash a powerful jutsu against {enemy}!\n")
            exec(current_enemy_health)
            print()
            last_choice = attack_button
            if enemy_health > 0:
                exec(under_attack_message)
                print()
                health = health - firebolt_damage
                exec(current_health)
                exec(current_enemy_health)
                print()
            else:
                exec(current_health)
                exec(current_enemy_health)
                print()
        else:
            print(f"\nInvalid selection. Please type either '{attack_button}' or '{defend_button}'.\n")
        break

    if health <= 0:
        print("------------------\n")
        print(f"Oh No! {enemy} defeated you! You must wake up or all will be lost!")
        print("\n")
        break

    if enemy_health <= 0:
        print("------------------------------------\n")
        print("The legendary Madara Uchiha has been defeated!")
        print()
        print(
            f"Despite being one of the most powerful ninjas in history, you still defeated {enemy}. Congratulations!\n")
        print("You will surely become the next Hokage!\n")
        time.sleep(3)
        break

print("Game Over\n\n")
print("[Hope you enjoyed my mini game! ~~Dominic DaCosta]\nPlease click 'run' button to play again")