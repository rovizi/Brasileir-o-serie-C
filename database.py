import requests

def buscar_dados_seriec_externos():
    """
    Busca os eventos esportivos da Série C do Brasil na API gratuita do TheSportsDB.
    """
    try:
        url = "https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e=Brazilian_Serie_C"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("event", []) or []
            
    except Exception as e:
        print(f"Erro ao conectar com a API externa da Série C: {e}")
        
    return []