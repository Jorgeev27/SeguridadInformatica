# This Python code snippet takes user input for a string (`cadena`) and a character (`caracter`). It
# then iterates over the numbers 0 to 9 and replaces each occurrence of those numbers in the input
# string with the specified character. Finally, it prints the modified string.

cadena = input("Cadena: ");
caracter = input("Caracter: ");
for i in range(10):
    cadena = cadena.replace(str(i), caracter);
print(cadena);