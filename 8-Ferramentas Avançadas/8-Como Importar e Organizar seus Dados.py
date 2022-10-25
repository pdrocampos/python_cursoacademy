PETRA4.info() #Verificar todas as informações

PETR4.head() #Informação das primeiras linhas "(25)"

PETR4.tail() #Informação das últimas linhas "(9)"

tickers = ['PETR4.SA','GGBR4.SA','MRVE3.SA','CVCB3.SA']
novos_dados = pd.DataFrame()
for t in tickers:
    novos_dados[t] = wb.DataReader(t, data_source='yahoo', start = '2010-1-1')['adj Close']
novos_dados.tail()
