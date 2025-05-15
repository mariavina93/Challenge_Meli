import requests
import pandas as pd
import os

# Crear carpeta 'data' si no existe
os.makedirs("data", exist_ok=True)

# Indicadores a consultar
indicators = {
    "IT.NET.USER.ZS": "internet_users_pct",
    "IT.CEL.SETS.P2": "mobile_subs_per_100",
    "NY.GDP.PCAP.CD": "gdp_per_capita"
}

base_url = "http://api.worldbank.org/v2/country/AR/indicator/{code}?format=json&date=2000:2023&per_page=1000"

dataframes = []

for code, column_name in indicators.items():
    url = base_url.format(code=code)
    response = requests.get(url).json()

    if isinstance(response, list) and len(response) > 1:
       entries = response[1]
       rows = []
       for item in entries:
           year = int(item["date"])
           value = item["value"] if item["value"] is not None else 0
           rows.append({"year": year, column_name: value})
       df = pd.DataFrame(rows)
       dataframes.append(df)
    else:
        print(f"Error al obtener datos de {code}")

# Unir los dataframes por 'year'
df_final = dataframes[0]
for df in dataframes[1:]:
    df_final = pd.merge(df_final, df, on="year", how="outer")

df_final = df_final.sort_values("year")

# Guardar CSV
df_final.to_csv("data/indicadores_argentina.csv", index=False)
print("Archivo 'indicadores_argentina.csv' actualizado con éxito.")
