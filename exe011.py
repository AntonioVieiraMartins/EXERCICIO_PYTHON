print('=-=-=-=-= Calculadora pintar parede =-=-=-=-=')
n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))
parede = n1*n2
print(f'A parede tem {parede:.2f} m² e será  necessário {parede/2:.2f} l de tinta para pintar a parede')