#To check if given number is odd ?
def is_odd(number):
    return number % 2 !=0
number = int(input("enter a number:"))
if is_odd(number):
    print(f"{number} is odd.")
else:
    print(f"{number} is not odd.")