# The code `cadena1 = input("Cadena1: "); cadena2 = input("Cadena2: ");` is prompting the user to
# input values for two variables, `cadena1` and `cadena2`. The `input()` function is used to take user
# input from the console. The text "Cadena1: " and "Cadena2: " are displayed as prompts to the user
# before they enter their input. The values entered by the user will be stored in the variables
# `cadena1` and `cadena2` respectively.

cadena1 = input("Cadena1: ");
cadena2 = input("Cadena2: ");

# This block of code is checking if `cadena2` is a sub-string of `cadena1`.

if cadena1.find(cadena2) >- 1:
    print("La cadena2 es subcadena de cadena1");
else:
    print("La cadena2 no es subcadena de cadena1");

# The line `print(cadena1 if cadena1 < cadena2 else cadena2);` is using a conditional expression to
# determine which string to print.

print(cadena1 if cadena1 < cadena2 else cadena2);