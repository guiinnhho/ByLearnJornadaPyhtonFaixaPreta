"""
temperatura = 'quente'

print(temperatura)

if temperatura == 'quente':
    print('Vou tomar coca')
else:
    print('Vou tomar um Chocolate!\n E Assistir Série')

horario = 'noite'

if horario == 'Manhã':
    print('O Sol está Quente.')
elif horario == 'Tarde':
    print('O Por do Sol está chegando')
else:
    print('A lua está linda')

idade = 23

if idade >= 18:
    print('Você ja pode beber.')
else:
    print('Você ainda não pode beber')

temp = 32

if temp <= 30:
    print('Aceitavvel')
else:
    print('Estou derretendo')

# Valido, 1, 3, 6, 10
# INvalido, qualquer outro


num = int(input('Informe um numero de 1 a 10: '))

while (num >= 10) and (num < 0):
    if (num == 1) or (num == 3) or (num == 6) or (num == 10):
        print('É Válido!')
        break
    else:
        print('Não é Válido:')
    num = int(input('Informe um número válido: '))
print('Obrigado!')

# for          num           in range(1, 10)
# Para cada    num           no
for num in range(1, 10):
    print(num)

nome = ['Diogo', 'Emily', 'Alaka']

for nome in nome:
    print(f'O nome atual é: {nome}')
    if nome == 'Diogo':
        print('Sou eu.')

notas = [6, 7.5, 9, 10]
print(sum(notas))
soma = sum(notas)
print('A média é : ', soma / len(notas))

# Toda Função é uma rotina:

# Eu defino (def) uma rotina e a executo quants vezes que eu quiser.
# é uma execelente forma de deixar nosso código dinâmico e sem repetição

def nome_funcao():
    # Código da Função
    print('Código da Função')

# Chamando a Função
nome_funcao()

def mostar_nome():
    input('Diogo')

mostar_nome()

# PARÂMETRO / ARGUMENTO DA FUNÇÃO

def mostrar_nome(nome_atual):
    print(nome_atual)

mostrar_nome('Diogo')
mostrar_nome('Emily')

def cal_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

media_calculada = cal_media(8, 5)
print(media_calculada)
"""

# Cálculo IMC


def num_quadrado(numero):
    quadrado = numero * numero
    return quadrado


def cal_imc(peso, altura):
    altura_quadrada = num_quadrado(altura)
    meu_imc = peso / altura_quadrada

    return meu_imc


def classificar_imc(meu_imc):
    if imc < 18.5:
        resp = 'Magreza'
    elif (imc >= 18.5) and (imc < 25):
        resp = 'Normal'
    elif (imc >= 25) and (imc < 30):
        resp = 'SobrePeso'
    elif (imc >= 30) and (imc < 40):
        resp = 'Obesidade'
    else:
        resp = 'Obesidade Grave'

    return resp


# Entrada
nome = input('Informe seu nome: ')
peso = int(input(f'{nome}, informe seu peso: '))
altura = float(input(f'{nome}, informe agora sua altura: '))

# Processamento
imc = round(cal_imc(peso, altura), 2)
situacao = classificar_imc(imc)

# Saída
print(f'\n{nome} o seu IMC é: {imc} \nE sua situação é: {situacao}')

