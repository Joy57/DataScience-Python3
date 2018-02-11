import numpy as np

A = np.random.normal(31.0, 5.0, 10)
print (A) #will print a distribution around 31

#Lists
x = [1, 2, 3, 4, 5, 6] 
print(len(x)) 

print (x[:3]) #take a subset of the list, prints the first 3 elements

print (x[3:]) #prints everything after 3

print (x[-2:]) #prints the last two elements

x.extend([12,17]) #extends the list by adding two nums at the end 
print(x) # [1, 2, 3, 4, 5, 6, 12, 17]

x.append(9)
print(x) #[1, 2, 3, 4, 5, 6, 9]

#this below demonstrates that 
#in python, you can put whatever kind of data wherever you want
#you can put strings, numbers, or add another list in it.
y = [10, 11, 12]
listOfLists = [x, y]
print (listOfLists) # [[1, 2, 3, 4, 5, 6, 12, 17], [10,11,12]]

#reference to single element of a list 
print(y[1]) #prints 11

#built in sort function
z = [3, 2, 1]
z.sort()
print(z) # 1, 2, 3

z.sort(reverse=True) #allows you to sort in reverse order
print(z)