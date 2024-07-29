# This Python code prompts the user to enter two numbers, `num1` and `num2`. It then calculates the
# sum of these two numbers and checks if the sum is positive, negative, or zero. Depending on the
# result, it prints out a corresponding message:
# - If the sum is greater than 0, it prints "La suma es positiva" (The sum is positive).
# - If the sum is less than 0, it prints "La suma es negativa" (The sum is negative).
# - If the sum is equal to 0, it prints "La suma es cero" (The sum is zero).

num1 = int(input("Dime un número: "));
num2 = int(input("Dime otro número: "));

if(num1 + num2 > 0):
    print("La suma es positiva");
elif(num1 + num2 < 0):
    print("La suma es negativa");
else:
    print("La suma es cero");