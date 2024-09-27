from time import sleep
import random
print('Suas opções\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
escolha = int(input('Digite sua jogada: '))
pc = random.randint(0,2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if escolha == pc:
    if escolha == 0:
        print('Vocês esolheram PEDRA')
    elif escolha == 1:
        print('Vocês escolheram PAPEL')
    else:
        print('Vocês escolheram TESOURA')
    print('Deu empate')
else:
    if escolha == 0 and pc == 1:
        print(f'Você escolheu PEDRA. Computador escolheu PAPEL')
        print(f'Computador venceu')
    elif escolha == 1 and pc == 0:
        print(f'Você escolheu PAPEL. Computador escolheu PEDRA')
        print(f'Jogador venceu')
    elif escolha == 2 and pc == 1:
        print(f'Você escolheu TESOURA. Computador escolheu PAPEL')
        print('Jogador venceu')
    elif escolha == 1 and pc == 2:
        print(f'Você escolheu PAPEL. Computador escolheu TESOURA')
        print('Computador venceu')
    elif escolha == 2 and pc == 0:
        print(f'Você escolheu TESOURA. Computador escolheu PEDRA')
        print('Computador venceu')
    elif escolha == 0 and pc == 2:
        print(f'Você escolheu PEDRA. Computador escolheu TESOURA')
        print('Jogador venceu')
