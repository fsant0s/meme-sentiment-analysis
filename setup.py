from asyncio.windows_events import NULL
from csv import reader
import yaml
import os

dic = {}
dic['ROOT_DIR'] = os.path.abspath('')

with open("config.yaml", "r+") as file:
    try:
        configs = yaml.safe_load(file)
        if not (configs.get('ROOT_DIR', 0)) :
            yaml.dump(dic, file)       
    except yaml.YAMLError as exc:
        print(exc)
        
