import yaml

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