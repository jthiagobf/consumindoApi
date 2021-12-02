import requests


def main():
    print('####################')
    print('####################')
    print('### consulta cep ###')

    cep_input = input('Digite o cep para a consulta: ')

    if len(cep_input) != 8:
        print('quantidade errada de dígitos')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adress_data = request.json()

    if 'erro' not in adress_data:
        print('===> CEP Encontrado <===')
        print('CEP: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('Complemento: {}'.format(adress_data['complemento']))
        print('Bairro: {}'.format(adress_data['bairro']))
        print('Localidade: {}'.format(adress_data['localidade']))
        print('UF: {}'.format(adress_data['uf']))
        print('DDD: {}'.format(adress_data['ddd']))
    else:
        print('{}: CEP inválido'.format(cep_input))

    n_consulta = int(input('Deseja realizar uma nova consulta?\n1. Sim \n2. Sair '))

    if n_consulta == 1:
        main()
    else:
        print('Obrigado por utilizar!')


if __name__ == '__main__':
    main()
