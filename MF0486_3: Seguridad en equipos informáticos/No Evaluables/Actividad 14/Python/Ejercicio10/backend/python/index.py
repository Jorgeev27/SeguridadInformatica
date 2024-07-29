# This Python code prompts the user to input a username and password. It then checks if the entered
# username is "jorge" and the entered password is "pru". If both conditions are met, it prints
# "Bienvenido, Jorge!". Otherwise, it prints "Usuario o contraseña incorrectos.", indicating that the
# username or password entered was incorrect.

usuario = input ("Usuario: ");
contrasenia = input ("Contraseña: ");

if usuario == "jorge" and contrasenia == "pru":
    print ("Bienvenido, Jorge!");
else:
    print ("Usuario o contraseña incorrectos.");