# This Python code snippet is calculating the perimeter and area of a triangle.

base = float(input("Dime la base: "));
altura = float(input("Dime la altura: "));
ladoA = float(input("Dime el lado A: "));
ladoB = float(input("Dime el lado B: "));
perimetro = base + ladoA + ladoB;
area = base * altura / 2;
print("El perímetro es:", perimetro);
print("El área es:", area);