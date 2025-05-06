nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print("Sua média foi" ,media, "seu conceito foi A e você está APROVADO")
elif media >= 7.5 and media < 9:
    print("Sua média foi" ,media, "seu conceito foi B e você está APROVADO")  
elif media >= 6 and media < 7.5:
    print("Sua média foi" ,media, "seu conceito foi C e você está APROVADO")    
elif media >= 4  and media < 6:
    print("Sua média foi" ,media, "seu conceito foi D e você está REPROVADO")
elif media >= 0 and media < 4:
    print("Sua média foi" ,media, "seu conceito foi E e você está REPROVADO")                    