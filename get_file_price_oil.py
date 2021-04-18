#####################################################################################################
##
##  Get Data Engine
##
##  Author: Manilson Antonio Lussati
##  Date:   04/02/2021
##
#####################################################################################################

import time
import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import schedule

URI = 'https://oilprice.com/oil-price-charts/#prices'

def get_list_from_data(str_data):
    list_str_data = str_data.split('(')
    return list_str_data[0]


def replace_specific(text):
    
    text = text.replace('(2 \tdays Delay)', '')
        
    return text

    
def get_df_from_page_html():   
    req = requests.get(URI)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all("table", class_="oilprices__table")
    table_str = str(table)
    df = pd.read_html(table_str)[2]
    df_g = pd.read_html(table_str)[1]

    # Juntando os dados
    print('Juntando os dados')
    df_g = df_g[df_g[1].isin(['Girassol SellBuy'])]
    df = df[df[1].isin(['Cabinda SellBuy', 'Nemba SellBuy', 'Dalia SellBuy'])]

    df_join = df.append(df_g, ignore_index=True)

    print('DATAFRAME G: ', len(df_g))
    print('DATAFRAME : ', len(df))
    print('DATAFRAME JOIN: ', len(df_join))
    try:
        # Fazendo o tratamento dos dados
        df_join.rename(columns = {1:'pocos', 2:'price', 3:'change', 4:'%_change'}, inplace = True)
        df_join['pocos']       = df_join['pocos'].str.replace('SellBuy','')
        df_join['%_change']    = df_join['%_change'].apply(replace_specific)
        df_join.drop([0, 5], axis=1, inplace=True)
        df_join['%_change'] = df_join['%_change'].apply(get_list_from_data)
        df_join['data'] = datetime.today().strftime('%Y-%m-%d')
        df_join.reset_index(drop=True)
        df_join.to_excel('data/price_oil_{}.xlsx'.format(datetime.today().strftime('%Y-%m-%d')), index = False, header=True)
        print(df_join)
        return 'Done'
    except Exception as e:
        print('Alguma coisa deu errado: ', e)
        return e
    
def main():
    get_df_from_page_html()

if __name__ == '__main__':
    main()