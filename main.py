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
    siafi = adress_data['siafi']
    gia = adress_data['gia']
    ibge = adress_data['ibge']


    texto = f''' 
    Cep: {cep}
    Logradouro: {logradouro}
    Complemento: {complemento}
    Bairro: {bairro}
    Localidade: {localidade}
    UF: {uf}
    DDD: {ddd}
    
    --------------------
    Outras informações:
    
    SIAFI: {siafi}
    GIA (Apenas SP): {gia}
    Código do IBGE: {ibge}
    
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

obs_1 = Label(janela, text='*SIAFI = Sistema Integrado de Administração Financeira')
obs_1.grid(column=0, row=5, padx=15, pady=10)

obs_2 = Label(janela, text='*GIA = Guia de informação e apuração do ICMS')
obs_2.grid(column=0, row=6, padx=15, pady=10)



janela.mainloop()
