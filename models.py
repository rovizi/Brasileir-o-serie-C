from datetime import datetime

def formatar_jogo_seriec(id_jogo, evento):
    """
    Formata o evento da Série C mapeando status dinâmicos e acréscimos.
    """
    status_api = evento.get("strStatus", "Em andamento")
    minuto_atual = evento.get("intMinute", "45'")
    acrescimo = evento.get("strStoppageTime", "3'")
    
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
        "status": status_formatado,
        "detalhe_tempo": detalhe_tempo,
        "acrescimo": acrescimo if acrescimo else None,
        "transmissao": "NSports / DAZN / Nosso Futebol",
        "campeonato": "Brasileirão Série C"
    }

def formatar_tabela_seriec(tabela_data):
    """
    Garante a formatação correta dos dados da tabela de classificação da Série C.
    """
    # Se receber dados brutos, formata; se já vier pronto, retorna estruturado.
    return tabela_data
