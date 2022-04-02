import random
import time

def randomfursona():
    species = ["deer","wolf","dog"]
    colors = ["red","green","blue"]
    ns = random.choice(species)
    cs = random.choice(colors)
    print(f"Color: {cs}\nSpecies: {ns}\n")
    if ns == "wolf" and cs == "blue":
        print(f"Your fursona is a {cs} {ns}")
    else:
        print("Making new fursona...\n")
        time.sleep(3)
        randomfursona()

randomfursona()