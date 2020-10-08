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
