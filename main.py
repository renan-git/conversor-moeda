import requests
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def converter():
    try:
        converter = [key for key, value in moedas.items() if value == moeda_origem.get()]
        para = [key for key, value in moedas.items() if value == moeda_destino.get()]
        url = f'https://economia.awesomeapi.com.br/json/last/{converter[0]}-{para[0]}'
        valor = float(valor_entry.get())
        response = requests.get(url)
        data = response.json()
        cotacao = float(data[f'{converter[0]}{para[0]}']['bid'])
        conversao_label.config(text=f'{valor:.2f} {converter[0]} = {cotacao*valor:.2f} {para[0]}')
    except:
        messagebox.showwarning(title='Preencha os campos corretamente', message=f"Aviso!\nNão deixe campos vazios\nO campo valor recebe números inteiros ou decimais, por exemplo: 10.25\nNão é possível converter a mesma moeda")

window = Tk()
window.title("Conversor de Moeda")
window.minsize(height=220, width=300)

moedas = {
    "USD": "Dólar Americano (USD)",
    "BRL": "Real Brasileiro (BRL)",
    "EUR": "Euro (EUR)",
    "GBP": "Libra Esterlina (GBP)",
    "CHF": "Franco Suiço (CHF)"
}

opcoes = list(moedas.values())

conversor_moedas_label = Label(text="Conversor de Moedas", font=("Calibri", 18, "bold"))
conversor_moedas_label.pack()

valor_label = Label(text="Digite o valor", font=("Verdana", 8))
valor_label.pack()

valor_entry = Entry(width=28, justify="center")
valor_entry.pack()

converter_label = Label(text="Converter de", font=("Verdana", 8))
converter_label.pack()

moeda_origem = StringVar()
converter_combobox = Combobox(window, textvariable=moeda_origem, values=opcoes, state="readonly", width=25)
converter_combobox.pack()

para_label = Label(text="Para", font=("Verdana", 8))
para_label.pack()

moeda_destino = StringVar()
para_combobox = Combobox(window, textvariable=moeda_destino, values=opcoes, state="readonly", width=25)
para_combobox.pack()

converter_button = Button(text="Converter", command=converter)
converter_button.pack(pady=10)

conversao_label = Label(text="", font=("Verdana", 12))
conversao_label.pack()

window.mainloop()