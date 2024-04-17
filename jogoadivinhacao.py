import random;
print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = random.randrange(1,10)
#print(numeroSecreto)

#Definindo o número de tentativas
numeroTentativas = 10

rodada=1

while( rodada <= numeroTentativas):
    print('tentativas',rodada, 'de', numeroTentativas)

#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condiçõeseString = input('Digite um número: ')
   
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
 #numeroTentativas = numeroTentativas-1
#Aula Elif 26.02.24
    rodada = rodada + 1

    print('qual o nivel de dificuldade?')
    print("(1)-fácil, (2)-médio, (3)-dificil")
     
     nivel = int(input("defina o nivel:" ))