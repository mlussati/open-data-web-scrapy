import yaml
import pandas as pd


def get_list_from_data(str_data):
    list_str_data = str_data.split('(')
    return list_str_data[0]


def replace_specific(text):
    
    text = text.replace('(2 \tdays Delay)', '')
        
    return text

def read_parse_yaml():
    
    with open("settings/config.yaml", 'r') as stream:
        try:
            return (yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            return exc

def read_exist_file(file_read):
    try:
        df_oil = pd.read_excel(file_read)
        return df_oil
    except Exception as e:
        return e