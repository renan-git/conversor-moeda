import requests
from tkinter import *
from tkinter.ttk import *

def converter(moeda_origem, moeda_destino):
    pass

window = Tk()
window.title("Conversor de Moeda")
window.minsize(height=300, width=500)

moedas = {
    "USD": "Dólar Americano (USD)",
    "BRL": "Real Brasileiro (BRL)",
    "EUR": "Euro (EUR)",
    "GBP": "Libra Esterlina (GBP)",
    "BTC": "Bitcoin (BTC)",
    "ETH": "Ethereum (ETH)",
    "BNB": "Binance Coin (BNB)",
    "SOL": "Solana (SOL)"
}

opcoes = list(moedas.values())

conversor_moedas_label = Label(text="Conversor de Moedas", font=("Calibri", 24, "bold"))
conversor_moedas_label.pack()

valor_label = Label(text="Digite o valor", font=("Verdana", 8))
valor_label.pack()

valor_entry = Entry(width=30)
valor_entry.pack()

converter_label = Label(text="Converter de", font=("Verdana", 8))
converter_label.pack()

moeda_origem = StringVar()
converter_combobox = Combobox(window, textvariable=moeda_origem, values=opcoes, state="readonly")
converter_combobox.pack()

para_label = Label(text="Para", font=("Verdana", 8))
para_label.pack()

moeda_destino = StringVar()
para_combobox = Combobox(window, textvariable=moeda_destino, values=opcoes, state="readonly")
para_combobox.pack()

converter_button = Button(text="Converter", command=converter(moeda_origem, moeda_destino))

window.mainloop()

# def teste():
#     moeda_origem = input('Moeda Origem: ')
#     moeda_destino = input('Moeda Destino: ')
#     valor = float(input('Valor: '))
#
#     # quanto 1 moeda origem vale em moeda destino
#     url = f'https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'
#
#     response = requests.get(url=url)
#     data = response.json()
#     cotacao = float(data[f'{moeda_origem}{moeda_destino}']['bid'])
#     print(data)
#     print(f'{valor:.2f}{moeda_origem} = {round(cotacao*valor, 2)}{moeda_destino}')