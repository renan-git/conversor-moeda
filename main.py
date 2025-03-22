import requests

moeda_origem = input('Moeda Origem: ')
moeda_destino = input('Moeda Destino: ')
valor = float(input('Valor: '))

# quanto 1 moeda origem vale em moeda destino
url = f'https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'

response = requests.get(url=url)
data = response.json()
cotacao = float(data[f'{moeda_origem}{moeda_destino}']['bid'])
print(data)
print(f'{valor:.2f}{moeda_origem} = {round(cotacao*valor, 2)}{moeda_destino}')