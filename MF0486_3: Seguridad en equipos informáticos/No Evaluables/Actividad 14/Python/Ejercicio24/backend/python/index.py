# The code `cadena = input("Cadena: "); lista = cadena.split();` is taking user input for a string and
# then splitting that string into a list of words based on whitespace. The user is prompted to enter a
# string when the program runs, and that string is stored in the variable `cadena`. The `split()`
# method is then used on the `cadena` string to split it into a list of words, which are stored in the
# variable `lista`.

cadena = input("Cadena: ");
lista = cadena.split();

# This code snippet is iterating over each word in the list `lista` and printing the first character
# of each word without a newline character. After iterating through all the words, it prints a newline
# character to move to the next line.

for palabra in lista:
    print(palabra[0], end = "");
print();

# This code snippet is iterating over each word in the list `lista` and printing the capitalized
# version of each word with a space character at the end. The `capitalize()` method is used to
# capitalize the first letter of each word while keeping the rest of the word in lowercase. The `end =
# " "` argument in the `print()` function ensures that each word is printed with a space character
# after it, instead of moving to a new line. Finally, after iterating through all the words and
# printing the capitalized versions, a newline character is printed to move to the next line.

for palabra in lista:
    print(palabra.capitalize(), end = " ");
print();

# This code snippet is iterating over each word in the list `lista` and checking if each word starts
# with either the letter "a" or "A" using the `startswith()` method. If a word meets this condition,
# it is printed without moving to a new line. The `print(palabra, end = " ")` statement ensures that
# the words meeting the condition are printed with a space character after each word. Finally, after
# iterating through all the words in the list, a newline character is printed to move to the next
# line.

for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print(palabra, end = " ");
print();