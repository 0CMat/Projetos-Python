import random  # Import da função de aleatório

# Entrada do número limite para adivinhar
number_limit = int(
    input('\033[1m' + 'Computador:' + '\033[0m Digite o número correto entre 1 a '))


def guess(number_limit):  # Função para adivinhar
    # Criação do número aleatório
    random_number = random.randint(1, number_limit)
    list_incorrects_numbers = []  # Lista para número já tentados e incorretos
    # Entrada para número correto
    luck_number = int(
        input('\033[1m' + 'Computador:' + '\033[0m Adivinhe o número:\n'))

    if luck_number != random_number:  # Condição para verificar número correto
        # Inserção do número incorreto a lista
        list_incorrects_numbers.append(luck_number)
        while luck_number != random_number:  # Loop While até acertar o valor correto
            print('<------------------------------------------>')
            print('\033[1m' + 'Computador:' +
                  '\033[0m Não foi esse número, tente novamente!')
            print('\033[1m' + 'Computador:' +
                  '\033[0mTentativa de números:', list_incorrects_numbers)
            print('<------------------------------------------->')

            chosen_number = int(  # Inserção para verificação do número escolhido
                input('\033[1m' + 'Computador:' + '\033[0m Adivinhe o número:\n'))

            if chosen_number <= number_limit:  # Verificação do número escolhido, caso se  encaixa dentro dos limites estabelecidos
                luck_number = chosen_number
                list_incorrects_numbers.append(luck_number)
                print('\033[1m' + 'Computador:' + '\033[0m Ok, vou verificar!')
            else:
                print('------------------ ATENÇÃO -------------------------')
                print(
                    '\033[1m' + 'Computador:' + '\033[0m Escolha um valor dentro do limite estipulado.\nNúmeros de 1 a', number_limit)
                print('------------------ ATENÇÃO -------------------------')
    print('\033[1m' + 'Computador:' +
              '\033[0m Parabéns! Você acertou!!!\n Sabia que você iria conseguir!')


guess(number_limit)  # Chamada da função de adivinhar
