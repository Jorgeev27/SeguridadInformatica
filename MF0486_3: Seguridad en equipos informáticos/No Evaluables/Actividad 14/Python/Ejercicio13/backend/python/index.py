# This Python code prompts the user to enter a number, which is then stored in the variable `numero`.
# It then iterates through a loop from 1 to 10 (inclusive) and for each iteration, it prints the
# iteration number, the stored number `numero`, and the result of multiplying the iteration number by
# `numero`. This effectively prints the multiplication table for the entered number up to 10.

numero = int(input("Ingrese un número: "));

for cont in range(1, 11):
    print(cont, "*" ,numero, "=", cont * numero);