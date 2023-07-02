#List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)


print("*********************")
#list of even numbers between 0 and 18
nums = [i*2 for i in range(10)]
print(nums)


print("*****************************")
#squares of even numbers from 1 to 10
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
