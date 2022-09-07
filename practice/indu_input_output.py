# Python input / output
a = input("Enter any number")
print(f"The entered number is {a}, type is {type(a)}")

try:
    a = int(a)
except ValueError as ve:
    print(f"cannot convert because : {ve}")
exit(1)
