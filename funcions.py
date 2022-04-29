import pandas as pd
import json, requests

def getJson(url):
    jsonData = requests.get(url)
    data = json.loads(jsonData.text)
    df = pd.DataFrame(data['items'])
    return df

def getEntes():
    return getJson('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')

def getUF():
    entes = getEntes()
    lista_uf = entes['uf'].unique()
    lista_uf = lista_uf[lista_uf != None]
    lista_uf = sorted(lista_uf)
    return lista_uf

def getEntesPorUF(uf):
    entes = getEntes()
    return entes.loc[(entes['uf'] == uf), ['cod_ibge', 'ente']].sort_values(by='ente')

def getEntePorCodigoIbge(cod_ibge):
    entes = getEntes()
    ente = entes[(entes['cod_ibge'] == int(cod_ibge))]
    return ente.iloc[0]

def numero_inteiro(number):
    num = f'{number:_.0f}'
    return num.replace('_','.')

def to_moeda(number):
    num = f'{number:_.2f}'
    return num.replace('.', ',').replace('_','.')