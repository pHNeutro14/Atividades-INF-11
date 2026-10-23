pesoTotal = float(input("Insira o valor total do KG do peixe: "))

if pesoTotal > 50:
    excesso = pesoTotal - 50
    multa = excesso * 4
    print(f"Excedeu {excesso}kg - A multa será de R${multa}")

else: 
    print("Não excedeu, tenha um bom dia!!!!!!!!!!")