from datetime import datetime

def formatar_jogo_seriec(id_jogo, evento):
    """
    Formata o evento da Série C mapeando status dinâmicos:
    - Em andamento / Contando o tempo
    - Intervalo (com indicador visual)
    - Acréscimos (exibindo o card de tempo extra no canto)
    """
    status_api = evento.get("strStatus", "Em andamento")
    minuto_atual = evento.get("intMinute", "45'") # Exemplo de campo de minuto da API externa ou calculado
    acrescimo = evento.get("strStoppageTime", "3'") # Exemplo de acréscimo vindo da fonte
    
    # Lógica inteligente de status baseada no andamento da partida
    status_formatado = status_api
    detalhe_tempo = minuto_atual

    # Tratamento específico para Intervalo
    if status_api.lower() in ["intervalo", "ht", "halftime"]:
        status_formatado = "Intervalo"
        detalhe_tempo = "Descanso (HT)"
    elif status_api.lower() in ["encerrado", "ft", "full time"]:
        status_formatado = "Encerrado"
        detalhe_tempo = "Fim de Jogo"
    else:
        status_formatado = "Em andamento"
        detalhe_tempo = f"{minuto_atual}"

    return {
        "id": id_jogo + 1,
        "rodada": evento.get("intRound", "Rodada Atual"),
        "selecao": evento.get("strHomeTeam"),
        "logo_selecao": evento.get("strHomeTeamBadge", ""),
        "adversario": evento.get("strAwayTeam"),
        "logo_adversario": evento.get("strAwayTeamBadge", ""),
        "estadio": evento.get("strVenue", "Estádio da Série C"),
        "data": evento.get("dateEvent"),
        "horario": evento.get("strTime"),
        "placar": f"{evento.get('intHomeScore', '0')} x {evento.get('intAwayScore', '0')}",
        "status": status_formatado,            # Ex: "Em andamento", "Intervalo", "Encerrado"
        "detalhe_tempo": detalhe_tempo,        # Ex: "45'+3'" ou "HT"
        "acrescimo": acrescimo if acrescimo else None, # Card exibido no cantinho com o tempo extra (ex: "+3'")
        "transmissao": "NSports / DAZN / Nosso Futebol",
        "campeonato": "Brasileirão Série C"
    }
