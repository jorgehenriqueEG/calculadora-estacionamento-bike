def calcular_estacionamento(horas, tipo_bike):
    taxa_hora = 5.0
    total = horas * taxa_hora
    if tipo_bike == 'pro':
        total = total * 0.5
    return total

if __name__ == '__main__':
    print('--- Estacionamento Bike ---')
    try:
        horas = int(input('Quantas horas? '))
        tipo = input('Tipo da bike (road/pro): ')
        valor = calcular_estacionamento(horas, tipo)
        print(f'Valor a pagar: R$ {valor:.2f}')
    except ValueError:
        print('Entrada inválida.')