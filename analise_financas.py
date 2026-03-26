import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE3NTU1LCJpYXQiOjE3NzQ1MjU1NTUsImp0aSI6IjcwMDA4ODAxNzI0NjQyNGU4Y2FkODE4OTUwZjYzY2E2IiwidXNlcl9pZCI6Ijk1In0.XZ0cOvobMFDAch9x0Q0lCOoTonMGw-Rn2scTLq800i0"

resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2025-03-21"},
)

print("status:", resp.status_code)
print("content-type:", resp.headers.get("Content-Type"))
print("texto da resposta:")
print(resp.text)

# Filtrar empresa com maior ROE
dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roe", "p_vp"]]
df2["rank_roe"] = df2["roe"].rank()
df2["rank_p_vp"] = df2["p_vp"].rank(ascending=True)
df2["rank_final"] = (df2["rank_roe"] + df2["rank_p_vp"]) / 2
df2.sort_values("rank_final", ascending=False)


maximo = df["roe"].max()
filtro = df["roe"]==maximo
df[filtro]

#Backtest
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
params = {"ticker": "BBSE3", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
print(resp.json())
dados = resp.json()
df_preco = pd.DataFrame(dados)
print(df_preco)
print(df.columns)

filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, "fechamento"].iloc[0]
preco_final = float(preco_final)

filtro2 = df_preco["data"]=="2025-03-21"
preco_inicial = df_preco.loc[filtro2, "fechamento"].iloc[0]
preco_inicial = float(preco_inicial)
preco_final / preco_inicial -1


# API para pegar do IBOV

import yfinance as yf
# Get a ticker data
# teste back 1 ano
ibov = yf.download("^BVSP", start="2025-03-21", end="2026-03-26")
ibov.columns
# Esta como index a data dai vc faz ibov.index
filtro_1 = ibov.index == "2025-03-21"
preco_inicial_ibov = ibov[filtro_1]["Close"].iloc[0]

filtro_2 = ibov.index == "2026-03-23"
preco_final_ibov = ibov[filtro_2]["Close"].iloc[0]
print(preco_final_ibov)
preco_final_ibov / preco_inicial_ibov -1

import yfinance as yf
# Get a ticker data
# teste back 5 ano
ibov = yf.download("^BVSP", start="2021-03-21", end="2026-03-26")
ibov.columns
# Esta como index a data dai vc faz ibov.index
filtro_1 = ibov.index == "2021-03-25"
preco_inicial_ibov = ibov[filtro_1]["Close"].iloc[0]

filtro_2 = ibov.index == "2026-03-23"
preco_final_ibov = ibov[filtro_2]["Close"].iloc[0]
print(preco_final_ibov)
preco_final_ibov / preco_inicial_ibov -1





base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
params = {"ticker": "ibov", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
print(resp.json())
dados = resp.json()
df_ibov = pd.DataFrame(dados)
print(df_ibov)


filtro3 = df_ibov["data"]=="2026-03-23"
preco_final_ibov = df_ibov.loc[filtro3, "fechamento"].iloc[0]
preco_final_ibov = float(preco_final_ibov)

filtro4 = df_ibov["data"]=="2025-03-21"
preco_inicial_ibov = df_ibov.loc[filtro4, "fechamento"].iloc[0]
preco_inicial_ibov = float(preco_inicial_ibov)
preco_final_ibov / preco_inicial_ibov -1
