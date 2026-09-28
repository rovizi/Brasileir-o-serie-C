def formatar_jogo_seriec(i, evento):
    score_home = evento.get("intHomeScore")
    score_away = evento.get("intAwayScore")
    str_status = evento.get("strStatus", "")
    
    # Detecção de status baseada no andamento
    if "HT" in str_status or "Half Time" in str_status or "Intervalo" in str_status:
        status = "Intervalo"
    elif score_home is not None and score_away is not None:
        if "Final" in str_status or "Match Finished" in str_status:
            status = "Encerrados"
        else:
            status = "Tempo Real"
    else:
        status = "Agendados"

    placar = f"{score_home} x {score_away}" if score_home is not None and score_away is not None else "VS"

    return {
        "id": i + 1,
        "rodada": evento.get("intRound", "Rodada Atual"),
        "selecao": evento.get("strHomeTeam", "Mandante"),
        "logo_selecao": evento.get("strHomeTeamBadge", ""),
        "adversario": evento.get("strAwayTeam", "Visitante"),
        "logo_adversario": evento.get("strAwayTeamBadge", ""),
        "estadio": evento.get("strVenue", "Estádio não informado"),
        "pais": evento.get("strCountry", "Brasil"),
        "data": evento.get("dateEvent", "Em breve"),
        "horario": evento.get("strTime", "A definir"),
        "placar": placar,
        "status": status,
        "detalhe_tempo": str_status or "Normal",
        "transmissao": evento.get("strTV", "Placar Oficial da API"),
        "ocorrencias": {
            "cartoes_amarelos": evento.get("strYellowCards", "Nenhum"),
            "cartoes_vermelhos": evento.get("strRedCards", "Nenhum"),
            "substituicoes": evento.get("strSubstitutions", "Nenhuma")
        },
        "campeonato": "Brasileirão Série C",
    }
