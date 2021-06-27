#####################################################################################################
##                                                                                                 ##
##  Get Data Engine                                                                                ##
##                                                                                                 ##
##  Author: Palanca data Community                                                                 ##
##  Date:   04/02/2021                                                                             ##
##                                                                                                 ##
#####################################################################################################

import pandas as pd
import requests
import logging

from library.lib_treatment import replace_specific, get_list_from_data, read_parse_yaml
from datetime import datetime
from bs4 import BeautifulSoup


logging.basicConfig(format='%(asctime)s %(message)s', filename='logs/logstatus_aplication.log', level=logging.INFO)

def get_df_from_page_html():   

    try:

        req = requests.get(read_parse_yaml()['url'])

        if req.status_code == 200:
            logging.info('Started, sucess request')
            content = req.content

        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find_all("table", class_="oilprices__table")
        table_str = str(table)
        
        df = pd.read_html(table_str)[2]
        df_g = pd.read_html(table_str)[1]

        # Juntando os dados
        logging.warning('Juntando os dados')
        df_g = df_g[df_g[1].isin(['Girassol SellBuy'])]
        df = df[df[1].isin(['Cabinda SellBuy', 'Nemba SellBuy', 'Dalia SellBuy'])]

        df_join = df.append(df_g, ignore_index=True)

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

            logging.warning(df_join.head)
            logging.info('Finished')

        except Exception as e:
            logging.error('Alguma coisa deu no tratamento dos dados: ', exc_info=e)
            return e

    except Exception as e:
            logging.error('Alguma coisa deu errado: ', exc_info=e)
            return e
def main():
    get_df_from_page_html()

if __name__ == '__main__':
    main()