from cmath import log
from get_file_price_oil import main
# Schedule Library imported
import schedule
import logging
import time
  
# Functions setup

def execute_main_function():
    try:
        main()
        print("Executando a funcao principal")
    except Exception as e:
        logging.error('Alguma coisa deu errado: ', exc_info=e)
        return e

# Task scheduling
# Todos os dias as 20:05 horas. 
schedule.every().day.at("20:06").do(execute_main_function)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)