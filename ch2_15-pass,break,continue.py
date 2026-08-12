print("befor loop line")
for i in range(1):
    pass

print("after loop line print using pass key word")
for x in range(1,6):
    if x == 2 :
        continue
    print(x)
print('\n')

        
for y in range(1,6):
    if y == 2 :
        break
    print(y)
