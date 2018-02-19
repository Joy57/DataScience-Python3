for x in range(10):
    print(x)
#above will print from 0 to 9 

for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print(x)
    #prints 0 to 5

x = 0
while (x < 10):
    print(x)
    x += 1
#prints 0 to 9