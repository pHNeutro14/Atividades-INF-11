num1 = int(input("Insira o 1° número: "))
num2 = int(input("Insira o 2° número: "))
num3 = int(input("Insira o 3° número: "))

if num1 >= num2 >= num3 or num2 >= num1 >= num3:
    print("O numero 3 é o menor: ", num3)

elif num3 >= num2 >= num1 or num2 >= num3 >= num1:
    print("O numero 1 é o menor: ", num1)

elif num3 >= num1 >= num2 or num1 >= num3 >= num2:
    print("O numero 2 é o menor: ", num2)

if num1 <= num2 <= num3 or num2 <= num1 <= num3:
    print("O numero 3 é o maior: ", num3)

elif num3 <= num2 <= num1 or num2 <= num3 <= num1:
    print("O numero 1 é o maior: ", num1)

elif num3 <= num1 <= num2 or num1 <= num3 <= num2:
    print("O numero 2 é o maior: ", num2)
