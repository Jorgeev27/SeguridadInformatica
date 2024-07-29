# This Python code snippet is a program that prompts the user to input a month number. Based on the
# input provided by the user, the program then determines and prints out the number of days in that
# particular month.

mes = int(input("Mes:"));

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("El mes tiene 31 días");
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días");
elif mes == 2:
    print("El mes tiene 28 días (si dicho año no es bisiesto)");
else:
    print("Mes inválido");