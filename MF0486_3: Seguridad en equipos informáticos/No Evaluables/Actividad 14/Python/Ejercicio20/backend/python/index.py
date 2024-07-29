# The line `lista = ["Di", "buen", "día", "a", "Jorge", "hola", "Jorge", "buen", "día"];` is creating
# a list called `lista` with the following elements: "Di", "buen", "día", "a", "Jorge", "hola",
# "Jorge", "buen", "día". Each element in the list is a string.

lista = ["Di", "buen", "día", "a", "Jorge", "hola", "Jorge", "buen", "día"];

# This part of the code is asking the user to input a string and then checking if that string is
# present in the list called `lista`. If the input string is found in the list, it prints "La cadena
# está en la lista." (The string is in the list). Otherwise, it prints "La cadena no está en la
# lista." (The string is not in the list).

cadena = input("Dime una cadena: ");
if cadena in lista:
    print("La cadena está en la lista.");
else:
    print("La cadena no está en la lista.");

print("Número de veces que aparece la cadena:", lista.count(cadena));

# This part of the code is performing a string replacement operation in the list `lista`. Here's a
# breakdown of what each line is doing:

cadena2 = input("Dime otra cadena para reemplazar: ");
apariciones = lista.count(cadena);
pos = 0;
for i in range(apariciones):
    pos = lista.index(cadena, pos);
    lista[pos] = cadena2;
    pos += 1;
print("Nueva lista:", lista);