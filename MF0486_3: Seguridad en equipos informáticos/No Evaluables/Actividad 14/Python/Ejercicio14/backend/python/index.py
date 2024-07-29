# This Python code calculates the factorial of a given number entered by the user.

num = int(input("Dime un número: "))
fact = 1;
for i in range(2, num + 1):
    fact *= i;
print("El factorial de", num, "es", fact);