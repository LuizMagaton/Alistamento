from datetime import date
ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

print (f"{dia_atual}/{mes_atual}/{ano_atual}")

ano = int(input("Qual ano voce nasceu?: "))
mes = int(input("Qual mes voce nasceu?: "))
dia = int(input("Qual dia voce nasceu?: "))

idade = ano_atual - ano
diferenca_ano = idade - 18
diferenca_mes = mes_atual - mes
diferenca_dia = dia_atual - dia

if idade == 18:
    print("A hora é agora, Vá se alistar!")
elif idade < 18:
    print (f"Precisara se alistar daqui à {diferenca_ano} anos {diferenca_mes} meses {diferenca_dia} dias")
else:
    print (f"Já se alistou hà {diferenca_ano} ano {diferenca_mes} meses {diferenca_dia} dias")

