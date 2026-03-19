import requests
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTUwMDc5LCJpYXQiOjE3NzM5NTgwNzksImp0aSI6ImJhMWE2MTFmNGMzMzRhZWNiMzFlNzQ5YjA4OGRlM2NmIiwidXNlcl9pZCI6Ijk1In0.m09V6Lx9HGZ_sZ_EhYjoLo4f4gQFk00KQoSywvVsmc4"
resp = requests.get(
    f"{base_url}/bolsa/preco-planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"ticker": "PETR4"},
)
print(resp.json())