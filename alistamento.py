from datetime import date

# Data atual
hoje = date.today()
print(hoje.strftime("%d/%m/%Y"))

ano = int(input("Qual ano voce nasceu?: "))
mes = int(input("Qual mes voce nasceu?: "))
dia = int(input("Qual dia voce nasceu?: "))

nascimento = date(ano, mes, dia)

alistamento = date(ano + 18, mes, dia)

if hoje == alistamento:
    print("A hora é agora, Vá se alistar!")
elif hoje < alistamento:
    diferenca = alistamento - hoje
    print(f"Precisará se alistar daqui a {diferenca.days // 365} anos, {(diferenca.days % 365) // 30} meses e {(diferenca.days % 365) % 30} dias")
else:
    diferenca = hoje - alistamento
    print(f"Já passou do alistamento há {diferenca.days // 365} anos, {(diferenca.days % 365) // 30} meses e {(diferenca.days % 365) % 30} dias")
