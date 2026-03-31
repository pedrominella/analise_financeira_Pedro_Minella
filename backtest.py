import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE3NTU1LCJpYXQiOjE3NzQ1MjU1NTUsImp0aSI6IjcwMDA4ODAxNzI0NjQyNGU4Y2FkODE4OTUwZjYzY2E2IiwidXNlcl9pZCI6Ijk1In0.XZ0cOvobMFDAch9x0Q0lCOoTonMGw-Rn2scTLq800i0"

resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)

print("status:", resp.status_code)
print("content-type:", resp.headers.get("Content-Type"))
print("texto da resposta:")
print(resp.text)

# Filtrar empresa com maior ROE
dados = resp.json()
df = pd.DataFrame(dados)
dados
df2 = df[["ticker", "roic", "earning_yield"]]
df2["rank_roic"] = df2["roic"].rank(ascending=False)
df2["rank_earning_yield"] = df2["earning_yield"].rank(ascending=False)
df2["rank_final"] = (df2["rank_earning_yield"] + df2["rank_earning_yield"]) / 2
df2.sort_values("rank_final", ascending=False)["ticker"][:20]

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

filtro2 = df_preco["data"]=="2021-04-01"
preco_inicial = df_preco.loc[filtro2, "fechamento"].iloc[0]
preco_inicial = float(preco_inicial)
preco_final / preco_inicial -1


import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"

tickers = ["BRKM5", "BRKM3", "RNEW11", "RNEW4", "TEKA4", "RIAA3", "AALR3", "APER3", "TOKY3", "SBFG3", "GOLL54", "SOMA3", "TCNO3", "TCNO4", "PRNR3", "ENJU3", "BRML3", "AZUL53", "ELMD3"]


resultados = []   # <- lista para guardar todos os resultados

for ticker in tickers:
    params = {
        "ticker": ticker,
        "data_ini": "2021-04-01",
        "data_fim": "2026-03-31"
    }

    resp = requests.get(
        f"{base_url}/preco/corrigido",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )

    dados = resp.json()
    df_preco = pd.DataFrame(dados)

    if df_preco.empty:
        print(f"Sem dados para {ticker}")
        continue

    df_preco["data"] = pd.to_datetime(df_preco["data"])
    df_preco["fechamento"] = pd.to_numeric(df_preco["fechamento"], errors="coerce")
    df_preco = df_preco.sort_values("data")

    preco_inicial = df_preco.iloc[0]["fechamento"]
    preco_final = df_preco.iloc[-1]["fechamento"]
    retorno = preco_final / preco_inicial - 1

    resultados.append({   # <- adiciona um resultado novo sem apagar os anteriores
        "ticker": ticker,
        "preco_inicial": preco_inicial,
        "preco_final": preco_final,
        "retorno": retorno
    })

df_resultados = pd.DataFrame(resultados)[:20]
print(df_resultados)

df_resultados.columns
df_resultados["resultado_ajustado"] = df_resultados['retorno'] * 0.05
print(df_resultados)
df_resultados['resultado_ajustado'].sum()

