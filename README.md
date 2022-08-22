print("----------------------| CARTERA DIGITAL |----------------------")


adc = False
fatura =[]
valid_valor = False
valid_conta = False
vezes = 0
total = 0



while salario == False
    sal_mes = input("Salário do mês: R$")
    try:
        sal_mes = float(valor)
        salario = True
    except:
        print("ERRO. Digite apenas números e separe os décimais com '.'.")

        
print("----------------------| FATURA DO MÊS |-------------------------")


while adc == False:

    while valid_conta == False:
        fat_mes = input("Instituição da conta. Ex: NuBank, Faculdade ")
        valid_conta =  True

    
    while valid_valor == False:
        valor = input("Valor da conta: R$ ")
        try:
            valor = float(valor)
            fatura.append([fat_mes,valor])
            total = total + valor
            valid_valor = True
        except:
            print("ERRO. Digite apenas números e separe os décimais com '.'.")
        

    sair = input("Deseja adicionar mais uma conta na fatura? (S ou N)").lower()
        
    if sair == "n":
        adc = True
    elif sair == "s":
        print("--------------------------------------------------------------------")
        vezes =+ 1
        valid_conta = False
        valid_valor = False
    else:
        print("ERRRO. Digite apenas 'S' ou 'N'.")
    


        
x = 1
por = (total * 100)/(sal_mes * x)

print (fatura)

print("| Razão Social:",fat_mes,"-  R$",valor,"|")
print("Valor total: R$",total)
print("Sua fatura é",por,"% do seu salário mensal.")
