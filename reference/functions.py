def squareIt(x):
    return x * x
print("squareIt call:")
print (squareIt(2))

#can pass func around as parameters
def DoSomething(f, x):
    return f(x)
print ("Call func DoSomething():")
print (DoSomething(squareIt, 3))

#lambda func let you inline simple func
print("Lambda call: ")
print (DoSomething(lambda x : x * x, 4))

# above code prints below lines
#squareIt call:
# 4
# Call func DoSomething():
# 9
# Lambda call:
# 16