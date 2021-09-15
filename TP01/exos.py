#print("Hello World")
import math

"""
x = int(input())
if x%2 == 0:
    print("it's even !")
else:
    print("it's odd !")
"""

"""
a = 56
b = 42

while a%b != 0:
    tmp = a%b
    a = b
    b = tmp
print(b)
"""

"""
total = 0
for i in range(2,42):
    if i%2==0:
        total+=i
print(total)
"""
"""
li = [5,9,10,2,32]
total = 0
for i in li:
    total+=i
print(total)
"""
#print([math.sqrt(x) for x in [5,9,1,25,8]])
#print([x for x in [5,9,1,24,8] if x%2==0])

def fact(x):
    """Returns the the factorial of an integer.

    Parameters:
        x (int):The integer which is to be calculed.

    Returns:
        fact(x):The integer which gets calculed."""
    return math.factorial(x)
print(fact(10))
help(fact)