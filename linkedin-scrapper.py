# -*- coding: utf-8 -*-

# Importações
from selenium import webdriver
from time import sleep

# Parâmetros
url = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'
arq_resultado = 'descricoes_vagas.txt'

# Execução do código
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    vagas = driver.find_elements_by_class_name('result-card')
    l_descricao = []
    erros = 0

    while True:
        for vaga in vagas:
            vaga.click()
            sleep(1)
            try:
                descricao = driver.find_element_by_class_name('description')
                l_descricao.append(descricao.text)
            except:
                print("Erro")
                erros +=1
                pass
        vagas = driver.find_elements_by_class_name('result-card')

        if len(l_descricao)+erros == len(vagas):
            break

    descricoes = '\n'.join(l_descricao)
    with open (arq_resultado, 'w') as f:
        f.write(descricoes)

    driver.quit()