word = input()
list = []
for i in range(len(word)):
    letter = word[i]

    if 65 <= ord(letter) <= 90:
        list.append(i)

print(list)
