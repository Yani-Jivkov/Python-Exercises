key = int(input())
n = int(input())
helper = []
for i in range(n):
    letter = input()
    helper.append(letter)
for i in range(n):
    helper[i] = chr(ord(helper[i]) + key)
print(''.join(helper))
