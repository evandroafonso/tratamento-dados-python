import pandas as pd
from twilio.rest import Client

# conta twilio
account_sid = "ACc758c580280cb0980a3656227d4dc53a"
# token twilio
auth_token  = "d17acde8fc0a22a7f3f9697c4d482c4f"
client = Client(account_sid, auth_token)

"""
passo a passo da solução:
- abrir os 6 arquivos em excel;
- meta 55.000
- para cada arquivo:
   - verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000;
   - se for maior que 55.000 o programa envia o SMS com nome, mês e as vendas do vendedor;
   - caso não seja maior que 55.000 o programa não terá nenhuma ação.
"""
listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listaMeses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')
    if (tabelaVendas ['Vendas'] > 55000).any():
        vendedor = tabelaVendas.loc[tabelaVendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[tabelaVendas ['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês de {mes} foi encontrado alguém que bateu a meta!! Vendedor(a) {vendedor} - Valor de vendas: R${vendas}')

        #envio de mensagem
        message = client.messages.create(
            to="+5541995082977",
            from_="+13474175306",
            body=f'Oi, Evandro')

        print(message.sid)


