from bs4 import BeautifulSoup
import requests

def acessar_pagina(link):
    """
    Responsável por acessar as páginas web
    """
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs

#TODO: extrair as informaçõe: numero da nota, titulo, link, data, horario
#TODO: percorrer todas as páginas 
#TODO: extrair o conteudo (parágrafos) de cada link
#TODO: inserir as informações em um arquivo JSON
#TODO: webscraping com selenium

def extrair_infos(lista_links):
    for link in lista_links:
        pagina= acessar_pagina(link)
        #find (encontra um elemento ou delimitar um pedaço da pagina)
        #find_all (encontra uma lista de elementos)
        lista_notas = pagina.find("div", atrrs={"id":"content-core"}).find_all("article")
        #print(len(lista_notas))
        for nota in lista_notas:
        #titulo
        #numero_nota (só numero)
        #linha
        #data
        #horario

            titulo = nota.h2.text.strip()
            link = nota.a["href"]
            try: 
                numero = nota.find("span", attrs={"class":"subtitle"}).text.strip().split()[-1]
            except AttributeError as erro:
                if str(erro) == "'NoneType' object has no attribute 'text'":
                    numero = "N/A"
            data = nota.find("span", attrs={"class":"summary-view-icon"})[0].text.strip()
            horario = nota.find("span", attrs={"class":"summary-view-icon"})[1].text.strip()
            print(titulo)
            print(link)
            print(f"Número da nota é: {numero}")
            print(data)
            print(horario)
            print("###")
        print("fim do loop for")

def percorrer_paginas(url_base):
    listas_de_links= []
    url_base = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=0"
    contador = 5010
    while contador>=0:
        link = url_base + str(contador)
        print(link)
        contador = contador - 30
        listas_de_links.append(link)
    return listas_de_links

def main(): 
    url_base = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=0" 
    lista_links = percorrer_paginas(url_base)
    extrair_infos(lista_links)
    #coletar_dados = extrair_infos()

if __name__ == "__main__":
    main()


