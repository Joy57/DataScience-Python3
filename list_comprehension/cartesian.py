#example
# A = {1, 3}
# B = {x, y}
# A  x B = {(1, x), (1, y), (3, x), (3, y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

#list_comprehension

# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test> and <test2>]
# [expr for val1 in collection1 and val2 in collection2]

cartesian_product = [(a, b) for a in A for b in B]
print (cartesian_product)