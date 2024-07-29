# This Python code is a simple number guessing game.

numSecreto = int(input("Dime un número secreto: "));
num = int(input("Adivina el número: "));
while num != numSecreto:
    if num > numSecreto:
        print("Tu número es menor");
    else:
        print("Tu número es mayor");
    num = int(input("Adivina el número: "));
print("Has acertado!");