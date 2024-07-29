# This Python code prompts the user to enter a number, then checks if the entered number is a prime
# number or not.

num = int(input("Dime un número: "));
numPrimo = True;
for cont in range(2, num):
    if num % cont == 0:
        numPrimo = False;
        break;
if numPrimo:
    print(num, "es un número primo");
else:
    print(num, "no es un número primo");