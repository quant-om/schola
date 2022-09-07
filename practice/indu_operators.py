# Python operators
# 1. Arithmetic operstors
# +, -, *, /, **, //, % are Arithmetic operstors
 
a = 2
b = 3
c = a + b
print(f"The sum of the variables is {c}")

c1 = a - b
print(f"The subtraction is {c1}")

c2 = a * b
print(f"The product is {c2}")

c3 = a / b
print(f"The division is {c3}")

c4 = a % b 
print(f"The remainder is {c4}")

c5 = a ** b 
print(f"The {a} power of {b} is {c5}")

c6 = a // b 
print(f"The quotient is {c6}")

# 2. Assignment operators
# =, +=, -=, *=, /=, !=, //=, %= are Assignment operators

# 3. Unary minus operator
a = 3
b = -(a)
print(f"the value of b is {b}")

# 4. Relational operators
# >, <, >=, <=, ==, !=
a = 7
b = 10
if a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print(f"{a} is greater than {b}")

if a != b:
    print(f"{a} is not equal to {b}")
else:
    print(f"{a} is equal to {b}")

# 5. Logical operators
# and , or, not are logical operators
a = 5
b = 8
c = 6
if (a>b) and (a>c):
    print(f"{a} is greater")
else:
    print(f"{a} is lesser")

if (c<a) or (c<b):
    print(f"it is true")
else:
    print(f"it is false")
if b != c:
    print(f"it is true")
else:
    print(f"it is false")



