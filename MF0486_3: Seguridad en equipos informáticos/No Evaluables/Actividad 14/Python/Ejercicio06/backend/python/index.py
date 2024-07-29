# This Python code snippet is asking the user to input a number of minutes, converting that input into
# an integer, and then calculating and displaying the corresponding hours and remaining minutes.

minutos = int(input("Dime los minutos: "));
print("Las horas son:", minutos // 60);
print("Los minutos restantes son:", minutos % 60);
print("Son:", minutos // 60, "horas y", minutos % 60, "minutos");