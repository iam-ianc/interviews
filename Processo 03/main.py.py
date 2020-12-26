from sys import exit
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

def exportExcel(configs, data):
  folderResult = 'excel'

  now = datetime.now()
  year = now.strftime('%Y')
  month = now.strftime('%B')
  day = now.strftime('%d')
  hour = now.strftime('%H')
  minute = now.strftime('%M')
  second = now.strftime('%S')
  dateToday = '-'.join([hour, minute, second, year, month, day])

  website = configs['website']
  params = configs['params']

  nameFile = f'{dateToday}-{website}-{params}.xlsx'
  pathFile = f'{folderResult}/{nameFile}'

  names = data[0]
  prices = data[1]
  content = list(zip(names, prices))

  if ( not os.path.isdir(folderResult) ):
    os.mkdir(folderResult)
  
  
  df = pd.DataFrame(content, columns=['Name', 'Price'])
  writer = pd.ExcelWriter(pathFile, engine="xlsxwriter")
  df.to_excel(writer, sheet_name='Sheet1', index = False, encoding='utf-8')
  writer.save()

  clear()
  print('Seu arquivo foi gerado com sucesso!')
  print(f'Seu arquivo: {nameFile} está disponível no diretório: {folderResult}')
  print('\nGoodbye *-*')
  exit()


def getSearch(configs):
  idWebsite = configs['idWebsite']
  url = configs['url']

  titles = []
  prices = []

  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')

  if (idWebsite == '1'):
    containerClass = 'ui-search-results'
    listOl = soup.select(f'section[class="{containerClass}"] ol')
    
    for arrLiOl in listOl:
      arrTitle = arrLiOl.find_all(class_='ui-search-item__title ui-search-item__group__element')

      # arrPrice = arrLiOl.find_all(class_='price-tag-fraction')
      arrDivPrice = arrLiOl.find_all(class_='ui-search-price ui-search-price--size-medium ui-search-item__group__element')
      
      for title in arrTitle:
        titles.append(title.get_text())
      for arrSpanPrice in arrDivPrice:
        price = arrSpanPrice.find_all('span', class_='price-tag-fraction')[0]
        prices.append(price.get_text())

  return [ titles, prices ]

def search():
  clear()
  print('*** O que deseja buscar? ***\n')
  txt = input('--> ').strip().lower()

  txt = txt.split(' ')
  txt = list(filter(None, txt))

  return txt

def configWebsite(idWebsite):
  params = search()

  if (idWebsite == '1'):
    website = 'MercadoLivre'
    # url = 'https://lista.mercadolivre.com.br/'
    url = 'https://lista.mercadolivre.com.br/'

    first = '-'.join(params)
    # second = '%20'.join(params)
    second = '_DisplayType_G'
    # query = f'{first}#D[A:{second}]'
    query = f'{first}{second}'

    newUrl = f'{url}{query}'
    return { 
      'idWebsite': idWebsite, 
      'website': website, 
      'url': newUrl,
      'params': first
    }

def chooseWebsite():
  choose = True

  while(choose):
    clear()
    print('*** Escolha um site para pesquisa: ***\n')
    print('-----> 1 - Mercado Livre:')
    print('-----> 3 - Sair\n')

    idWebsite = input('--> ')
    
    if (idWebsite == '1'):
      choose = False
      configUrl = configWebsite(idWebsite)
      # break
    elif (idWebsite == '3'):
      clear()
      print('\nGoodbye *-*')
      exit()
  
  return configUrl

def clear():
  return os.system('cls')

def main():
  configs = chooseWebsite()
  data = getSearch(configs)
  exportExcel(configs, data)

main()