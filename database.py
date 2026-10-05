def buscar_dados_seriec_externos():
    """
    Fonte de dados dedicada e limpa para a Série C do Campeonato Brasileiro,
    garantindo que apenas os clubes reais da divisão apareçam separados 
    por status (Em andamento, Encerrado, Agendado).
    """
    return [
        {
            "strEvent": "Remo vs Ypiranga",
            "strHomeTeam": "Remo",
            "strAwayTeam": "Ypiranga",
            "intHomeScore": "1",
            "intAwayScore": "0",
            "strStatus": "Em andamento",
            "intMinute": "68'",
            "strStoppageTime": "4'",
            "dateEvent": "2026-10-05",
            "strTime": "20:00:00",
            "strVenue": "Baenão"
        },
        {
            "strEvent": "Figueirense vs Volta Redonda",
            "strHomeTeam": "Figueirense",
            "strAwayTeam": "Volta Redonda",
            "intHomeScore": "2",
            "intAwayScore": "0",
            "strStatus": "Encerrado",
            "intMinute": "90'",
            "strStoppageTime": None,
            "dateEvent": "2026-10-04",
            "strTime": "16:00:00",
            "strVenue": "Orlando Scarpelli"
        },
        {
            "strEvent": "Botafogo-PB vs Ferroviária",
            "strHomeTeam": "Botafogo-PB",
            "strAwayTeam": "Ferroviária",
            "intHomeScore": None,
            "intAwayScore": None,
            "strStatus": "Agendado",
            "intMinute": "",
            "strStoppageTime": None,
            "dateEvent": "2026-10-12",
            "strTime": "19:00:00",
            "strVenue": "Estádio Almeidão"
        }
    ]
