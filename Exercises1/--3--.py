queue = input("")
animals = queue.split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    wolf_position = animals.index("wolf")
    sheep_position = len(animals) - wolf_position - 1
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
