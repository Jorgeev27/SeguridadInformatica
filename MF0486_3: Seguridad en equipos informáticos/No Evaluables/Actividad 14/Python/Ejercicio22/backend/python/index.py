# This Python code snippet takes user input for a string (`cadena`) and a character (`caracter`). It
# then uses the `join()` method to concatenate the character input between each character in the
# string input. Finally, it prints the resulting string with the character inserted between each
# character of the original string.

cadena = input("Cadena: ");
caracter = input("Caracter: ");
print(caracter.join(cadena));