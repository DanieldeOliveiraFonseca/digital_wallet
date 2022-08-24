

salario = False
adc = False
valid_valor = False
valid_conta = False
fatura = []
total = 0


print("----------------------| CARTERA DIGITAL |----------------------")


while salario == False:
    sal_mes = input("Salário do mês: R$")
    try:
        sal_mes = float(sal_mes)
        salario = True
    except:
        print("ERRO. Digite apenas números e separe os décimais com '.'.")


print("----------------------| FATURA DO MÊS |-------------------------")


while adc == False:

    while valid_conta == False:
        fat_mes = input("Instituição da conta (Ex: NuBank, Faculdade). ")

        valid_conta = True

    while valid_valor == False:
        valor = input("Valor da conta: R$ ")
        try:
            valor = float(valor)
            fatura.append([fat_mes, valor])
            total = total + valor
            valid_valor = True
        except:
            print("ERRO. Digite apenas números e separe os décimais com '.'.")

    sair = input(
        "Deseja adicionar mais uma conta na fatura? (S ou N) ").lower()

    if sair == "n":
        adc = True
    elif sair == "s":
        print("--------------------------------------------------------------------")
        valid_conta = False
        valid_valor = False
    else:
        print("ERRRO. Digite apenas 'S' ou 'N'.")

x = 1
por = (total * 100)/(sal_mes * x)
por1 = str(por)

saldoAtual = sal_mes - total
print("\n")
print("----------------------------FATURA-------------------------------")


for i in fatura:
    print("| " + str(i[0]) + " --->  R$" + str(i[1]) + " |")


print("TOTAL: R$"+str(total))
print("Sua fatura é", por1[0:4]+"% do seu salário mensal.")
print("Saldo Atual: R$" + str(saldoAtual))

sair = input("Precione ENTER para sair.")
