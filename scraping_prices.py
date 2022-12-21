import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


df = pd.read_csv('price.csv', sep=';')
print(df.loc[0][1])

produto = int(input('Qual produto você dejesa saber o valor?\n'
                    '[1] TVs\n'
                    '[2] Celulares\n'
                    '[3] Notebooks\n'))
preco = int(input('Qual a opção de valor gostaria de visualizar?\n'
                  '[1] Menor preço\n'
                  '[2] Maior Preço\n'
                  '[3] Melhor avaliado\n'))

url = df.loc[produto-1][preco]
xpath = r'/html/body/div[1]/div[1]/div/div[2]/div[3]/div[1]/a/div[2]/div[2]/div[2]/p[1]'

browser = webdriver.Chrome()
browser.get(url)
price = browser.find_element(By.XPATH, xpath).text

print(price)
