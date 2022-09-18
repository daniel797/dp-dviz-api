

# main.py
# =============================================================================
# common
import os
import json
# requirements
from dotenv import load_dotenv
from fastapi import FastAPI
import pandas as pd
# -----------------------------------------------------------------------------

load_dotenv('./.env')

app = FastAPI()

# => routers
@app.get('/')
async def mainIndex() -> ...:
    return main_index()

@app.get('/countries/{country_name}/years/{year}')
async def countryInfo(country_name: str, year: str) -> ...:
    return country_info(country_name, year)

# => functions
def main_index() -> dict:
    return {'message': 'use this api para tu viz'}

def country_info(country_name: str, year: str) -> dict:
    host_data = os.environ['HOST_DATA']
    
    data_mapper = {
        'peru': f'{host_data}/peru.csv',
        'colombia': f'{host_data}/colombia.csv',
        'chile': f'{host_data}/chile.csv',
        'argentina': f'{host_data}/argentina.csv',
        'mexico': f'{host_data}/mexico.csv'
    }
    country_data = data_mapper[country_name]
    
    df = pd.read_csv(country_data, sep=';', encoding='utf-8')
    subdf = df[df['year'] == int(year)]
    return json.loads(subdf.to_json(orient='records', date_format='iso'))
