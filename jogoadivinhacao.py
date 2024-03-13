print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = 38


#Definindo o número de tentativas
numeroTentativas = 3
rodada=1

while( rodada <= numeroTentativas):
    print('tentativas',rodada, 'de', numeroTentativas)

#Recebendo o chute do jogador
    chuteString = input('Digite um número: ')
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