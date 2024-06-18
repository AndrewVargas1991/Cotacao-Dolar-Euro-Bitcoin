# pip install requests
import requests

def cotacao():
	link = f'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
	requisicao = requests.get(link)
	requisicao = requisicao.json()
	dolar = float(f"{requisicao['USDBRL']['bid']}")
	euro = float(f"{requisicao['EURBRL']['bid']}")
	bitcoin = float(f"{requisicao['BTCBRL']['bid']}")

	print(f'Dolar: {dolar:.2f}'.replace('.',','))
	print(f'Euro: {euro:.2f}'.replace('.',','))
	print(f'Bitcoin: {bitcoin:_.2f}'.replace('.', ',').replace('_', '.'))

cotacao()

input('\nAperte ENTER para sair...')