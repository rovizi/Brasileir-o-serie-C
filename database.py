import requests

def buscar_dados_seriec_externos():
    """
    Fonte de dados oficial e real para a Série C.
    Conecta diretamente à API-Football para buscar os jogos, placares e status em tempo real,
    garantindo que os dados venham de uma fonte externa e verdadeira.
    """
    url = "https://v3.football.api-sports.io/fixtures"
    
    # Parâmetros para a Série C do Brasil (ID da liga e temporada atual)
    # Nota: O ID exato da Série C do Brasil na API-Football pode ser verificado na listagem de ligas deles.
    querystring = {"league": "14", "season": "2026"} 
    
    headers = {
        "x-rapidapi-key": "SUA_CHAVE_AQUI", # Substitua pela sua chave real da API-Football / RapidAPI
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            dados = response.json().get("response", [])
            
            eventos_formatados = []
            for item in dados:
                fixture = item.get("fixture", {})
                teams = item.get("teams", {})
                goals = item.get("goals", {})
                status = fixture.get("status", {})
                
                # Tratando a data e hora vindas da API
                data_completa = fixture.get("date", "")
                date_event = data_completa.split("T")[0] if "T" in data_completa else ""
                str_time = data_completa.split("T")[1][:8] if "T" in data_completa else "00:00:00"
                
                eventos_formatados.append({
                    "strEvent": f"{teams.get('home', {}).get('name')} vs {teams.get('away', {}).get('name')}",
                    "strHomeTeam": teams.get("home", {}).get("name"),
                    "strAwayTeam": teams.get("away", {}).get("name"),
                    "intHomeScore": str(goals.get("home")) if goals.get("home") is not None else None,
                    "intAwayScore": str(goals.get("away")) if goals.get("away") is not None else None,
                    "strStatus": status.get("short"), # Ex: 'FT' (Encerrado), 'NS' (Não iniciado), '1H' (Em andamento)
                    "intMinute": str(status.get("elapsed", "")) if status.get("elapsed") else "",
                    "strStoppageTime": None,
                    "dateEvent": date_event,
                    "strTime": str_time,
                    "strVenue": fixture.get("venue", {}).get("name", "Estádio não informado")
                })
            
            # Se a API retornar dados com sucesso, devolvemos a lista formatada
            if eventos_formatados:
                return eventos_formatados
                
    except Exception as e:
        print(f"Erro ao conectar na API real da Série C: {e}")
    
    # Fallback de segurança caso a requisição falhe ou retorne vazia
    return []
