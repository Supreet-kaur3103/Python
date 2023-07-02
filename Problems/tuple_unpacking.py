#numbers = (1, 2, 3)
#a, b, c = numbers
#print(a)
#print(b)
#print(c)

print("*****************")

x, y = [1, 2]
x, y = y, x
print("y=",y)

print("**************")
a, b, c, d, *e, f, g = range(20)
print("Length of e=",len(e))