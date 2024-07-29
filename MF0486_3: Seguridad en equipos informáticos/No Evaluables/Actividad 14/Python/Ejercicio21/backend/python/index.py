# This Python code snippet is creating a list called `listaNumeros` with elements `[2, 3, 4, 1]`.
# Then, it creates a copy of `listaNumeros` called `listaNumeros2` using slicing. Next, it sorts the
# original list `listaNumeros` in ascending order using the `sort()` method.

listaNumeros = [2, 3, 4, 1];
listaNumeros2 = listaNumeros[:];
listaNumeros.sort();
if listaNumeros == listaNumeros2:
    print("Lista ordenada");
else:
    print("Lista no ordenada");