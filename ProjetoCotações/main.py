import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests

# FAZENDO A REQUISIÇÃO PARA A API DE COTAÇÃO DE MOEDAS
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()

# ATRIBUINDO AS CHAVES DO DICIONÁRIO NA LISTA
lista_moedas = list(dicionario_moedas.keys())

# CRIANDO A JANELA
janela = tk.Tk()


# TITULO
janela.title('Sistema de Cotações')


# FUNÇÃO PARA PEGAR A COTAÇÃO E TRATAR O DADO OBTIDO.
def pegar_cotacao():
    try:
        moeda = combobox_selecionar_moeda.get()
        data_cotacao = calendario_moeda.get()
        # FATIANDO A STRING data_cotacao
        dia = data_cotacao[:2]
        mes = data_cotacao[3:5]
        ano = data_cotacao[6:]
        link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
        requisicao_moeda = requests.get(link)
        cotacao = requisicao_moeda.json()
        valor_moeda = cotacao[0]['bid']
        label_texto_cotacao['text'] = f'A cotação da  {moeda} no dia {data_cotacao} foi de R$ {valor_moeda}'
    except Exception:
        label_texto_cotacao['text'] = f'ERRO! SELECIONE UMA DATA!'


""" --- COTAÇÃO DE 1 MOEDAS  --- """

# TEXTO # BORDAS- TITULO
label_cotacoes_moeda = tk.Label(text='Cotação de 1 moeda específica', borderwidth=2, relief='solid', bg='#4777FF',
                                fg='white')
label_cotacoes_moeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe',
                          columnspan=3)  # PADX E PADY - DISTANCIA ENTRE OS OBJETOS

label_selecionar_moeda = tk.Label(text='Selecionar moeda', anchor='e')
label_selecionar_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)  # STICKY - CENTRALIZA

# CAIXA DE SELEÇÃO
combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

# TEXTO - SELECIONAR DIA DA COTAÇÃO
label_selecionar_dia = tk.Label(text='Selecione o dia que deseja pegar a cotação', anchor='e')
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# CALENDARIO DE DATAS
calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

# TEXTO RESULTADO DA COTAÇÃO
label_texto_cotacao = tk.Label(text='', borderwidth=2, relief='solid')
label_texto_cotacao.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky='nswe')

# BOTAO PEGAR COTAÇÃO
botao_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao, bg='#71C642')
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# BOTAO FECHAR - FINALIZAR
botao_fechar = tk.Button(text='Fechar', command=janela.quit, bg='red')
botao_fechar.grid(row=10, column=2, sticky='nswe', pady=10, padx=10)

# EXECUTANDO
janela.mainloop()
