text = input("")
text_lower = text.lower()

count_sand = text_lower.count("sand")
count_water = text_lower.count("water")
count_fish = text_lower.count("fish")
count_sun = text_lower.count("sun")

total_occurrences = count_sand + count_water + count_fish + count_sun

print(total_occurrences)
