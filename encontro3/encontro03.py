from bs4 import BeautifulSoup
import requests

def acessar_pagina(link):
    """
    Responsável por acessar as páginas web
    """
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    return bs

#TODO: extrair as informaçõe: numero da nota, titulo, link, data, horario
#TODO: percorrer todas as páginas 
#TODO: extrair o conteudo (parágrafos) de cada link
#TODO: inserir as informações em um arquivo JSON
#TODO: webscraping com selenium

def extrair_informações():
    link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=0"
    pagina= acessar_pagina(link)
    #find (encontra um elemento ou delimitar um pedaço da pagina)
    #find_all (encontra uma lista de elementos)
    lista_notas = pagina.find("div", atrrs={"id":"content-core"}).find_all("article")
    print(len(lista_notas))
    for nota in lista_notas:
        #titulo
        #numero_nota (só numero)
        #linha
        #data
        #horario

        titulo = nota.h2.text.strip()
        link = nota.a["href"]
        numero = nota.find("span", attrs={"class":"subtitle"}).text.strip().split()[-1]
        data - nota.find("i", attrs={"class":"icon-day"})
        print(titulo)
        print(f"Número da nota é: {numero}")
        print("###")
    print("fim do loop for")

def main(): 
    coletar_dados = extrair_informações()

if __name__ == "__main__":
    main()


