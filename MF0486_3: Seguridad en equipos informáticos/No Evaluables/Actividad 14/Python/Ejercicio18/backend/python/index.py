# This Python code snippet prompts the user to enter a number, stores the numbers in a list until a
# non-positive number is entered, then it finds and prints the maximum number in the list. After that,
# it iterates through the list to check and print which numbers are even. Finally, it uses list
# comprehension to print the even numbers in the list.

num = int(input("Dime un número: "));
listaNumeros = [];

while num > 0:
    listaNumeros.append(num);
    num = int(input("Dime otro número: "));
print("Maximo:", max(listaNumeros));
for n in listaNumeros:
    if n % 2 == 0:
        print("Numero par: ", n, end=" ");
print();
for n in[x for x in listaNumeros if x % 2 == 0]:
    print(n);