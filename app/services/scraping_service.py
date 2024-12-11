import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_producao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    linhas_tabela = table.find_all('tr')

    dados = []
    for linha in linhas_tabela:
        cells = linha.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        dados.append(cells_text)

    df = pd.DataFrame(dados[1:], columns=dados[0])
    return df

def get_processamento_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    linhas_tabela = table.find_all('tr')

    dados = []
    for linha in linhas_tabela:
        cells = linha.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        dados.append(cells_text)

    df = pd.DataFrame(dados[1:], columns=dados[0])
    return df

def get_comercializacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    linhas_tabela = table.find_all('tr')

    dados = []
    for linha in linhas_tabela:
        cells = linha.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        dados.append(cells_text)

    df = pd.DataFrame(dados[1:], columns=dados[0])
    return df

def get_importacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    linhas_tabela = table.find_all('tr')

    dados = []
    for linha in linhas_tabela:
        cells = linha.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        dados.append(cells_text)

    df = pd.DataFrame(dados[1:], columns=dados[0])
    return df

def get_exportacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    linhas_tabela = table.find_all('tr')

    dados = []
    for linha in linhas_tabela:
        cells = linha.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        dados.append(cells_text)

    df = pd.DataFrame(dados[1:], columns=dados[0])
    return df