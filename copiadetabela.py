from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.vriconsulting.com.br/guias/guiasIndex.php?idGuia=1")

xpath_da_tabela = '//*[@id="corpoGuia"]/table[1]/tbody'
tabela = driver.find_element("xpath", xpath_da_tabela)

linhas = tabela.find_elements("tag name", "tr")
dados = []
for linha in linhas:
    colunas = linha.find_elements("tag name", "td")
    dados.append([coluna.text for coluna in colunas])

driver.quit()

print(dados)


#df = pd.DataFrame(dados, columns=["N", "Campo", "Descrição", "Tipo", "Tam", "Dec", "Obrig"])
#print(df)

#df.to_csv("dados_da_tabela.csv", index=False)