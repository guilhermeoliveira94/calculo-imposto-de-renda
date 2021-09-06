salarioBruto = float(input('Informe o salário bruto:'))
numeroDependentes = int(input('Informe o número de dependentes:'))
deducaoDependentes = numeroDependentes * 189.59

calculoInss = salarioBruto
if calculoInss < 1045.01:
    inss = (calculoInss*7.5)/100
    inss = round(inss, 2)
elif 1045 < calculoInss > 2089.61:
    inss = (((calculoInss-1045)*9)/100)+78.38
    inss = round(inss, 2)
elif 2089.60 < calculoInss > 3134.41:
    inss = (((calculoInss-2089.60)*12)/100)+78.38+94.01
    inss = round(inss, 2)
elif 3134.41 < calculoInss > 6101.07:
    inss = (((calculoInss-3134.40)*14)/100)+78.38+94.01+125.37
    inss = round(inss, 2)
else:
    inss = (78.38+94.01+125.37+415.33)
    inss = round(inss,2)
print("Contribuição INSS: R$",inss,"reais")

if salarioBruto <= 1903.99:
    salarioLiquido = salarioBruto
    print("Desconto de Impostos de Renda: ISENTO")
    print("Salário Líquido: R$",salarioLiquido,"reais")
elif 1903.99 > salarioBruto <= 2826.66:
    desconto = ((salarioBruto-deducaoDependentes-inss*7.5)/100)-142.8
    desconto = round(desconto,2)
    salarioLiquido = salarioBruto - desconto
    salarioLiquido = round(salarioLiquido,2)
    print("Salário Bruto: R$",salarioBruto,"reais")
    print("Desconto de Impostos de Renda: R$",desconto,"reais")
    print("Salário Líquido: R$", salarioLiquido, "reais")
elif 2826.66 > salarioBruto <= 3751.06:
    desconto = ((salarioBruto-deducaoDependentes-inss*7.5)/100)-354.8
    desconto = round(desconto,2)
    salarioLiquido = salarioBruto - desconto
    salarioLiquido = round(salarioLiquido,2)
    print("Salário Bruto: R$",salarioBruto,"reais")
    print("Desconto de Impostos de Renda: R$",desconto,"reais")
    print("Salário Líquido: R$", salarioLiquido, "reais")
elif 3751.06 > salarioBruto <= 4664.69:
    desconto = ((salarioBruto-deducaoDependentes-inss*7.5)/100)-636.13
    desconto = round(desconto,2)
    salarioLiquido = salarioBruto - desconto
    salarioLiquido = round(salarioLiquido,2)
    print("Salário Bruto: R$",salarioBruto,"reais")
    print("Desconto de Impostos de Renda: R$",desconto,"reais")
    print("Salário Líquido: R$", salarioLiquido, "reais")
else:
    desconto = ((salarioBruto-deducaoDependentes-inss*7.5)/100)-869.36
    desconto = round(desconto,2)
    salarioLiquido = salarioBruto - desconto
    salarioLiquido = round(salarioLiquido,2)
    print("Salário Bruto: R$",salarioBruto,"reais")
    print("Desconto de Impostos de Renda: R$",desconto,"reais")
    print("Salário Líquido: R$", salarioLiquido, "reais")
