from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Função para acessar a página e coletar os títulos, segmentos, links e datas das notícias
def acessar_pagina_dinamica(link):
    # Configura e inicia o navegador
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)
    sleep(5)  # Espera a página carregar completamente

    # Coletar os títulos das notícias, seus segmentos, links e datas
    titulos_segmentos_links_datas = []
    segmentos = navegador.find_elements(By.CSS_SELECTOR, "[data-qa='ContentSections-SectionContainer'] span")
    titulos = navegador.find_elements(By.CSS_SELECTOR, "[data-qa='ContentHeadline-Headline']")
    links = navegador.find_elements(By.CSS_SELECTOR, "[data-qa='BaseLink-renderAnchor-StyledAnchor']")
    datas = navegador.find_elements(By.CSS_SELECTOR, "[data-qa='ContentActionBar-handleRenderDisplayDateTime-time']")

    for segmento, titulo, link, data in zip(segmentos, titulos, links, datas):
        titulos_segmentos_links_datas.append((segmento.text, titulo.text, link.get_attribute("href"), data.text))

    navegador.quit()  # Fecha o navegador

    return titulos_segmentos_links_datas

# Função para salvar os títulos, segmentos, links e datas em um arquivo de texto
def salvar_titulos_em_txt(titulos_segmentos_links_datas, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        for segmento, titulo, link, data in titulos_segmentos_links_datas:
            try:
                f.write(f"Segmento: {segmento}\n")
                f.write(f"Título: {titulo}\n")
                f.write(f"Link: {link}\n")
                f.write(f"Data: {data}\n")
                f.write("\n")
            except Exception as e:
                print(f"Erro ao adicionar título ao arquivo de texto: {e}")

# Função principal
def main():
    link = "https://www.scmp.com/news/china?module=oneline_menu_section_int&pgtype=homepage"
    titulos_segmentos_links_datas = acessar_pagina_dinamica(link)
    salvar_titulos_em_txt(titulos_segmentos_links_datas, "titulos_noticias.txt")

if __name__ == "__main__":
    main()
