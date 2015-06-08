# -*- coding: utf-8 -*-
from colorama import init, Fore
init()
print(Fore.RED)
print("""
    CircuitLab - Identificador de resistores""")

cores = {"1": "PRETO",
              "2": "MARROM",
              "3": "VERMELHO",
              "4": "LARANJA", 
              "5": "AMARELO",
              "6": "VERDE",
              "7": "AZUL",
              "8": "VIOLETA",
              "9": "CINZA",
              "10": "BRANCO",
              "11": "DOURADO",
              "12": "PRATEADO"}
              
lista_cores = ["PRETO","MARROM","VERMELHO","LARANJA",
"AMARELO","VERDE","AZUL","VIOLETA","CINZA","BRANCO","DOURADO","PRATEADO"]

def imprime_cores():
    for x,y in enumerate(lista_cores):
        print("(",x,")",y)
def TipoResistor():
    while True:    
        tipo =input("Qual é o tipo do resistor? 4 cores ou 5 cores?  ").strip().upper()              
        if tipo == "4" or tipo == "5":
            return tipo
        else:
            print("\nTipo inválido, digite 4 ou 5 para a quantidade de cores do resistor.")
tipo = TipoResistor()
def CoresResistor():
        if tipo == "4":
            while True:
                imprime_cores()        
                cor1 = input("Digite o número correspondente a cor da primeira listra: ")
                total=0
                if cor1=="0":
                    total+=0
                    break
                elif cor1=="1":
                    total+=100
                    break
                elif cor1=="2":
                    total+=200
                    break
                elif cor1=="3":
                    total+=300
                    break
                elif cor1=="4":
                    total+=400
                    break
                elif cor1=="5":
                    total+=500
                    break
                elif cor1=="6":
                    total+=600
                    break
                elif cor1=="7":
                    total+=700
                    break
                elif cor1=="8":
                    total+=800
                    break
                elif cor1=="9":
                    total+=900
                    break
                else:
                    print("Cor inválida. Digite um número de 0 a 9.")
            while True:    
                        imprime_cores()
                        cor2 = input("Digite o número correspondente a cor da segunda listra:")
                        if cor2=="0":
                            total+=0
                            break
                        elif cor2=="1":
                            total+=10
                            break
                        elif cor2=="2":
                            total+=20
                            break
                        elif cor2=="3":
                            total+=30
                            break
                        elif cor2=="4":
                            total+=40
                            break
                        elif cor2=="5":
                            total+=50
                            break
                        elif cor2=="6":
                            total+=60
                            break
                        elif cor2=="7":
                            total+=70
                            break
                        elif cor2=="8":
                            total+=80
                            break
                        elif cor2=="9":
                            total+=90
                            break
                        else:
                            print("Cor inválida. Digite um número de 0 a 9.")
            while True:            
                        imprime_cores()            
                        multiplicador = input("Digite o número correspondente a cor da terceira listra(multiplicador):")
                        mult=0
                        if multiplicador=="0":
                            mult = 1
                            break
                        elif multiplicador=="1":
                            mult=10
                            break
                        elif multiplicador=="2":
                            mult=100
                            break
                        elif multiplicador=="3":
                            mult=1000
                            break
                        elif multiplicador=="4":
                            mult=10000
                            break
                        elif multiplicador=="5":
                            mult=100000
                            break
                        elif multiplicador=="6":
                            mult=1000000
                            break
                        elif multiplicador=="7":
                            mult=10000000
                            break
                        elif multiplicador=="11":
                            mult=0.1
                            break
                        elif multiplicador=="12":
                            mult=0.01
                            break
                        else:
                            print("Cor inválida. Digite um número de 0 a 9 e 11 ou 12.")
            while True:    
                        toleran=0                                
                        tolerancia = input("Digite o número correspondente a cor da quarta listra(tolerância): ")
                        imprime_cores()
                        if tolerancia=="1":
                            toleran=1
                            break
                        elif tolerancia=="2":
                            toleran=2
                            break
                        elif tolerancia=="5":
                            toleran=0.5
                            break
                        elif tolerancia=="6":
                            toleran=0.25
                            break
                        elif tolerancia=="7":
                            toleran=0.1
                            break
                        elif tolerancia=="8":
                            toleran=0.05
                            break
                        elif tolerancia=="11":
                            toleran=5
                            break
                        elif tolerancia=="12":
                            toleran=10
                            break
                        else:
                            print("Cor inválida. Digite um número de entre 1,2,5,6,7,8,11,12.")
        elif tipo == "5":
            while True:
                imprime_cores()        
                cor1 = input("Digite o número correspondente a cor da primeira listra: ")
                total=0
                if cor1=="0":
                    total+=0
                    break
                elif cor1=="1":
                    total+=100
                    break 
                elif cor1=="2":
                    total+=200
                    break
                elif cor1=="3":
                    total+=300
                    break
                elif cor1=="4":
                    total+=400
                    break
                elif cor1=="5":
                    total+=500
                    break
                elif cor1=="6":
                    total+=600
                    break
                elif cor1=="7":
                    total+=700
                    break
                elif cor1=="8":
                    total+=800
                    break
                elif cor1=="9":
                    total+=900
                    break
                else:
                    print("Cor inválida. Digite um número de 0 a 9.")
            while True:    
                    imprime_cores()
                    cor2 = input("Digite o número correspondente a cor da segunda listra:")
                    if cor2=="0":
                        total+=0
                        break
                    elif cor2=="1":
                        total+=10
                        break
                    elif cor2=="2":
                        total+=20
                        break
                    elif cor2=="3":
                        total+=30
                        break
                    elif cor2=="4":
                        total+=40
                        break
                    elif cor2=="5":
                        total+=50
                        break
                    elif cor2=="6":
                        total+=60
                        break
                    elif cor2=="7":
                        total+=70
                        break
                    elif cor2=="8":
                        total+=80
                        break
                    elif cor2=="9":
                        total+=90
                        break
                    else:
                        print("Cor inválida. Digite um número de 0 a 9.")
            while True:    
                    imprime_cores()
                    cor3 = input("Digite o número correspondente a cor da terceira listra:")
                    if cor3=="0":
                        total+=0
                        break
                    elif cor3=="1":
                        total+=10
                        break
                    elif cor3=="2":
                        total+=20
                        break
                    elif cor3=="3":
                        total+=30
                        break
                    elif cor3=="4":
                        total+=40
                        break
                    elif cor3=="5":
                        total+=50
                        break
                    elif cor3=="6":
                        total+=60
                        break
                    elif cor3=="7":
                        total+=70
                        break
                    elif cor3=="8":
                        total+=80
                        break
                    elif cor3=="9":
                        total+=90
                        break
                    else:
                        print("Cor inválida. Digite um número de 0 a 9.")        
            while True:            
                    imprime_cores()            
                    multiplicador = input("Digite o número correspondente a cor da quarta listra(multiplicador):")
                    mult=0
                    if multiplicador=="0":
                        mult = 1
                        break
                    elif multiplicador=="1":
                        mult=10
                        break
                    elif multiplicador=="2":
                        mult=100
                        break
                    elif multiplicador=="3":
                        mult=1000
                        break
                    elif multiplicador=="4":
                        mult=10000
                        break
                    elif multiplicador=="5":
                        mult=100000
                        break
                    elif multiplicador=="6":
                        mult=1000000
                        break
                    elif multiplicador=="7":
                        mult=10000000
                        break
                    elif multiplicador=="11":
                        mult=0.1
                        break
                    elif multiplicador=="12":
                        mult=0.01
                        break
                    else:
                        print("Cor inválida. Digite um número de 0 a 9 e 11 ou 12.")
            while True:    
                    toleran=0                                
                    tolerancia = input("Digite o número correspondente a cor da quinta listra(tolerância): ")
                    imprime_cores()
                    if tolerancia=="1":
                        toleran=1
                        break
                    elif tolerancia=="2":
                        toleran=2
                        break
                    elif tolerancia=="5":
                        toleran=0.5
                        break
                    elif tolerancia=="6":
                        toleran=0.25
                        break
                    elif tolerancia=="7":
                        toleran=0.1
                        break
                    elif tolerancia=="8":
                        toleran=0.05
                        break
                    elif tolerancia=="11":
                        toleran=5
                        break
                    elif tolerancia=="12":
                        toleran=10
                        break
                    else:
                        print("Cor inválida. Digite um número de entre 1,2,5,6,7,8,11,12.")
            else:
                    print("Digite um número de listras igual a 4 ou 5")                     
        print (total*mult)
CoresResistor()


print("")            

            
        