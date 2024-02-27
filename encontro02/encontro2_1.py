from bs4 import BeautifulSoup
import requests
from pandas import pyarrow

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
    notas_imprensa = pagina.find("div", atrrs={"id":"content-core"}).find_all("article")
    print(notas_imprensa)
    for nota_imprensa in notas_imprensa:
        titulo = nota_imprensa.find("h2").text.strip()
        print(titulo)
        print("###")
    print("fim do loop for")

def main(): 
    pass

if __name__ == "__main__":
    main()


