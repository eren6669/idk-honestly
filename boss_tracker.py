player_name = "titeeksh"
character_level = 1
total_estus_flasks = 5
diamond = 0
print(f"--- welcome back, {player_name} ---")
print(f"current level: {character_level} | estus flasks: {total_estus_flasks}! | diamond: {diamond}") 
boss_name = input("dancer:")
deaths_input = input(f" KILLED BY {boss_name}:")
deaths = int(deaths_input)
import time 
if deaths == 0:
    print(f"HOLY SWEAT! You beat {boss_name} on your first try!")
    character_level = character_level + 5
    diamond = diamond + 10
elif deaths <= 5:
    print(f"DAMM TWIN! You mastered {boss_name}'s moveset quickly huh.")
    character_level = character_level + 2
    diamond = diamond + 5
else:
    print(f"LOCK IN GNG... {boss_name} absolutely railed you.")
    print("Loading your fate...")
    diamond = diamond + 0
time.sleep(1.5)
#\n is a newline character, imagine as if this key hits enter everytime you use it inna code line. it puts the letters after \n below the line 
print("\n--- STATS UPDATED ---")
print(f"character level: {character_level}")
print(f"total estus flasks: {total_estus_flasks}")
print(f"inventory diamonds: {diamond}") 
