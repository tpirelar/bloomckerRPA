import requests
from requests.structures import CaseInsensitiveDict
import json
import pandas as pd
import csv
import os

limpiaPantalla = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def wait(): 
    char = input('')

if __name__ == '__main__':
   
    url = 'https://covid19-api.com/country/all'
    
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    payload = { "format": 'json' }

    limpiaPantalla()
    response = requests.get(url, headers=headers, params=payload)
    
    if response.status_code == 200:
        
        columns = ('country', 'confirmed', 'recovered', 'critical', 'deaths')
        response_json = json.loads(response.text)
        
        for i in range(len(response_json)):
            country = response_json[i]['country']
            confirmed = response_json[i]['confirmed']
            recovered = response_json[i]['recovered']
            critical = response_json[i]['critical']
            deaths = response_json[i]['deaths']

            print('Country: ', country)
            print('Confirmed: ', confirmed)
            print('Recovered: ', recovered)
            print('Critical: ', critical)
            print('Deaths: ', deaths)
            print('*******************************************\n')
     
        
        df = pd.DataFrame(data=response_json)
        df.to_csv('listado_COVID19.csv', index=False, columns=columns, header=False)
        

    else:
        pass           