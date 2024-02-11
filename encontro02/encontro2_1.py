from bs4 import BeautifulSoup
import requests
import pandas as pd

def acessar_pagina(link):
    """
    Responsável por acessar as páginas web
    """
    pagina=requests.get(link)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    print(bs)
    return bs

def extrair_informações():
    link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    pagina= acessar_pagina(link)
    notas_imprensa = pagina.find_all("div", atrrs=("id":"content-core")).find_all("article")
    print(notas_imprensa)

def main(): 
    pass

if __name__ == "__main__":
    main()
