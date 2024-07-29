# This Python code snippet is asking the user to input a number. It then checks if the input number is
# even or odd by using the modulo operator `%`.

num = int(input("Dime un número: "));
if num % 2 == 0:
    print(num, "es par");
else:
    print(num, "es impar");