def formatar_jogo_seriec(i, evento):
    """
    Padroniza os dados brutos da API externa incluindo cartões, substituições e status de intervalo.
    """
    score_home = evento.get("intHomeScore")
    score_away = evento.get("intAwayScore")
    str_status = evento.get("strStatus", "")
    
    # Tratamento inteligente do status da partida (Intervalo, Ao Vivo, Finalizado, Agendado)
    if "HT" in str_status or "Half Time" in str_status or "Intervalo" in str_status:
        status = "Intervalo"
    elif score_home is not None and score_away is not None:
        if "Final" in str_status or "Match Finished" in str_status:
            status = "Finalizado"
        else:
            status = "Ao Vivo"
    else:
        status = "Agendados"

    # Capturando dados extras de ocorrências da partida (quando disponíveis na API)
    cartoes_amarelos = evento.get("strYellowCards", "Nenhum")
    cartoes_vermelhos = evento.get("strRedCards", "Nenhum")
    substituicoes = evento.get("strSubstitutions", "Nenhuma")

    placar = f"{score_home} x {score_away}" if score_home is not None and score_away is not None else "VS"

    return {
        "id": i + 1,
        "selecao": evento.get("strHomeTeam", "Mandante"),
        "adversario": evento.get("strAwayTeam", "Visitante"),
        "data": evento.get("dateEvent", "Em breve"),
        "horario": evento.get("strTime", "A definir"),
        "placar": placar,
        "status": status,
        "detalhe_tempo": str_status or "Normal",
        "ocorrencias": {
            "cartoes_amarelos": cartoes_amarelos,
            "cartoes_vermelhos": cartoes_vermelhos,
            "substituicoes": substituicoes
        },
        "campeonato": "Brasileirão Série C",
    }