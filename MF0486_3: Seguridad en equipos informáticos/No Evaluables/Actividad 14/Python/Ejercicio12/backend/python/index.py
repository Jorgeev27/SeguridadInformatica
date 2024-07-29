# This Python code prompts the user to input a letter. It then checks if the input is an uppercase
# letter (A-Z) or a lowercase letter (a-z) and prints a corresponding message indicating whether the
# input is uppercase or lowercase.

letra = input("Ingrese una letra: ");

if letra >= 'A' and letra <= 'Z':
    print("La letra es mayúscula");
elif letra >= 'a' and letra <= 'z':
    print("La letra es minúscula");