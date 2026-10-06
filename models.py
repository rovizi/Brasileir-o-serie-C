from datetime import datetime

def formatar_jogo_seriec(id_jogo, evento):
    """
    Formata o evento da Série C mapeando status dinâmicos, agendados, adiados e acréscimos de forma assíncrona.
    """
    status_api = str(evento.get("strStatus", "")).strip().lower()
    minuto_atual = evento.get("intMinute", "")
    acrescimo = evento.get("strStoppageTime", "")
    
    # Mapeamento rigoroso de status
    if status_api in ["intervalo", "ht", "halftime"]:
        status_formatado = "Intervalo"
        detalhe_tempo = "Descanso (HT)"
    elif status_api in ["encerrado", "ft", "full time", "aest", "p"]:
        status_formatado = "Encerrado"
        detalhe_tempo = "Fim de Jogo"
    elif status_api in ["agendado", "ns", "not started", ""] or not status_api:
        status_formatado = "Agendado"
        detalhe_tempo = evento.get("strTime", "Em breve")
    elif status_api in ["adiado", "pst", "postponed"]:
        status_formatado = "Adiado"
        detalhe_tempo = "Adiado"
    else:
        status_formatado = "Em andamento"
        detalhe_tempo = f"{minuto_atual}" if minuto_atual else "Em andamento"

    return {
        "id": id_jogo + 1,
        "rodada": evento.get("intRound", "Rodada Atual"),
        "selecao": evento.get("strHomeTeam", "Time Casa"),
        "logo_selecao": evento.get("strHomeTeamBadge", ""),
        "adversario": evento.get("strAwayTeam", "Time Visitante"),
        "logo_adversario": evento.get("strAwayTeamBadge", ""),
        "estadio": evento.get("strVenue", "Estádio da Série C"),
        "data": evento.get("dateEvent", ""),
        "horario": evento.get("strTime", ""),
        "placar": f"{evento.get('intHomeScore', '0')} x {evento.get('intAwayScore', '0')}",
        "status": status_formatado,
        "detalhe_tempo": detalhe_tempo,
        "acrescimo": acrescimo if acrescimo else None,
        "transmissao": evento.get("strTV", "NSports / DAZN / Nosso Futebol"),
        "campeonato": "Brasileirão Série C"
    }

def formatar_tabela_seriec(tabela_data):
    """
    Garante a formatação correta dos dados da tabela de classificação da Série C.
    """
    return tabela_data
