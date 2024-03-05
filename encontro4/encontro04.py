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
#TODO: try e except
#TODO: percorrer todas as páginas 
#TODO: extrair o conteudo (parágrafos) de cada link
#TODO: inserir as informações em um arquivo JSON
#TODO: webscraping com selenium  
#TODO: analise de dados     

def extrair_infos(percorre_paginas):
    for link in percorre_paginas:
        for nota_imprensa in notas_imprensa: 
            titulo = nota_imprensa.find('h2').text.strip()
            link = nota_imprensa.a["href"]
            tag_spam_data_horario = nota_imprensa.find_all ("span", attrs={"class":"summary-view-icon"})
            horario = tag_spam_data_horario[1].text.strip()
            numero_nota = nota_imprensa.find("span", attrs={"class":"subtitle"}).text.strip().split(" ")[-1]
            try: 
                numero_nota = nota.find("span", attrs={"class":"subtitle"}).text.strip().split()[-1]
            except AttributeError as erro:
                if str(erro) == "'NoneType' object has no attribute 'text'":
                    numero = "N/A"
            if numero_nota != "N/A":
                verificar = numero_nota.find("/")
                if verificar != 0:
                    numero_nota = numero_nota.split("/")[0]
            print(titulo)
            print(link)
            print(data)
            print(horario)
            print(numero_nota, type(numero_nota))
            conteudo = acessar_pagina(link)
            data_horario_atualizado = conteudo.find("span", attrs={"class": "documentModified"}).text
            print(data_horario_atualizado)
            data_atualizada = data_horario_atualizado[-2][3:]
            horario_atualizado= data_horario_atualizado[-1]
            print(data_atualizada)
            print(horario_atualizado)
            lista_paragrafos = conteudo.find("div", attrs={"property": "rnews:articleBody"}).find._all("p")
            paragrafos = []
            for tag_p in lista_paragrafos:
                paragrafo = tag_p.text.strip()
                paragrafos.append(paragrafo)
            print (paragrafos)
            print("###")

def percorrer_paginas(url_base):
    listas_de_links = []
    url_base = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int="
    contador = 5010
    while contador>=0:
        link = url_base + str(contador)
        print(link)
        contador = contador - 30
        listas_de_links.append(link)
    return listas_de_links

def main(): 
    percorre_paginas = percorrer_paginas
    extrair_infos(listas_de_links)
    #coletar_dados = extrair_infos()

if __name__ == "__main__":
    main()


