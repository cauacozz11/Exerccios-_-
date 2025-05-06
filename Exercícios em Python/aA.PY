# prod1 = float(input("Informe o preço do produto 1:" ))
# prod2 = float(input("Informe o preço do produto 2:" ))
# prod3 = float(input("Informe o valor do produto 3:" ))

# if prod1 == prod2 or prod1 == prod3 or prod2 == prod3:
#     print("os valores são iguais")     
# elif prod2 < prod1 and prod2 < prod3:
#     print(prod2)
# elif prod3 < prod1 and prod3 < prod2: 
#     print(prod3) 
# elif prod1 < prod2 and prod1 < prod3:
#     print(prod1)     

# num1 = int(input("informe um número:"))
# num2 = int(input("Informe um número: "))
# num3 = int(input("informe um número: "))

# if num1 >= num2 and num1 >= num3:
#     if num2 >= num3:
#         print("a ordem certa é:", num1,num2,num3)
#     else:
#         print("a ordme certa é:", num1,num3,num2) 
# elif num2 >= num1 and num2 >= num3:
#     if num1 >= num3:
#         print("a ordem certa é:", num2,num1,num3)
#     else:
#         print("a ordem certa é:", num2,num3,num1) 
# elif num3 >= num1 and num3 >= num2:
#     if num2 >= num1:
#         print("a ordem certa é:", num3,num2,num1)
#     else:
#         print("a ordem certa é:", num3,num1,num2)    
                       

# turno = (input("Informe o turno que você estuda, com M para matutino, V para vespertino e N para noturno: ")).upper()

# if turno == "M":
#     print("Bom dia!")
# elif turno == "V":
#     print("Boa Tarde!") 
# elif turno == "N":
#     print("Boa Noite!")    
# else:
#     print("Era M, V ou N burro")       


# salario = float(input("Informe o seu salário: "))

# if salario <= 280:
#     valor = salario * 0.2
#     salario1 =  salario + valor
#     print("Seu salário era: ", salario," Seu percentual de aumento foi de 20%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
# elif salario > 280 and salario <= 700:
#          valor = salario * 0.15
#          salario1 =  salario + valor
#          print("Seu salário era: ", salario," Seu percentual de aumento foi de 15%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
# elif salario > 700 and salario <= 1500:
#          valor = salario * 0.1
#          salario1 =  salario + valor
#          print("Seu salário era: ", salario," Seu percentual de aumento foi de 10%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
# elif salario < 1500:
#        valor = salario * 0.05
#        salario1 =  salario + valor
#        print("Seu salário era: ", salario," Seu percentual de aumento foi de 5%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)


# nota1 = float(input("informe a nota da dua primeira prova: "))
# nota2 = float(input("Informe a nota da primeira prova: "))

# media =  (nota1 + nota2) / 2 

# if media > 9 and media <= 10:
#     print("A, APROVADO")
# elif media >= 7.5 and media <= 9:
#     print("B, APROVADO")
# elif media >= 6 and media < 7.5:
#     print("C, APROVADO")
# elif media >= 4 and media < 6:
#     print("D, REPROVADO")
# elif media >= 0 and media < 4:
#     print("E, REPROVADO")
# else:
#     print("era entre 0 e 10 animal")               