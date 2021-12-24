import requests
from tkinter import *


def cep_input():
    cep = ed.get()
    return cep


def main():

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input()))

    adress_data = request.json()

    cep = adress_data['cep']
    logradouro = adress_data['logradouro']
    complemento = adress_data['complemento']
    bairro = adress_data['bairro']
    localidade = adress_data['localidade']
    uf = adress_data['uf']
    ddd = adress_data['ddd']

    texto = f''' 
    Cep: {cep}
    Logradouro: {logradouro}
    Complemento: {complemento}
    Bairro: {bairro}
    Localidade: {localidade}
    UF: {uf}
    DDD: {ddd}
     '''

    texto_cep['text'] = texto


janela = Tk()
janela.title('Consulta de CEP')

texto_inicial = Label(janela, text='Digite o número do CEP para obter informações (Apenas números)')
texto_inicial.grid(column=0, row=0, padx=15, pady=10)

ed = Entry(janela, text='')
ed.grid(column=0, row=1, padx=15, pady=10)

botao = Button(janela, text='Buscar CEP', command=main)
botao.grid(column=0, row=2, padx=15, pady=10)

texto_cep = Label(janela, text='')
texto_cep.grid(column=0, row=3, padx=15, pady=10)

novo_texto = Label(janela, text='Obrigado por utilizar !')
novo_texto.grid(column=0, row=4, padx=15, pady=10)


janela.mainloop()
