n = int(input())
open_brackets = False
closed_brackets = False
for i in range(n):
    data = input()
    if data == '(' and open_brackets == False:
        open_brackets = True
        continue
    elif data == '(' and open_brackets == True:
        print(f'UNBALANCED')
        exit()
    elif data == ')' and open_brackets == True:
        open_brackets = False
        continue
    elif data == ')' and open_brackets == False:
        print(f'UNBALANCED')
        exit()
print(f'BALANCED')