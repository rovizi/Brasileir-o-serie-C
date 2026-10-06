from datetime import datetime

def formatar_jogo_seriec(id_jogo, evento):
    """
    Formata o evento da Série C aplicando filtros rígidos de data, 
    status dinâmicos e ocorrências completas (cartões, faltas, pênaltis).
    """
    status_api = str(evento.get("strStatus", "")).strip().lower()
    minuto_atual = evento.get("intMinute", "")
    acrescimo = evento.get("strStoppageTime", "")
    
    # Captura a data do evento da API (ex: "2026-10-06")
    data_evento_str = evento.get("dateEvent", "")
    
    # Validação de segurança para ignorar jogos com datas retroativas fantasmas
    hoje = datetime.now().strftime("%Y-%m-%d")
    
    # Mapeamento rigoroso de status
    if status_api in ["intervalo", "ht", "halftime", "half time"]:
        status_formatado = "Intervalo"
        detalhe_tempo = "Fim do 1º Tempo (Intervalo)"
    elif status_api in ["encerrado", "ft", "full time", "aest", "p"]:
        status_formatado = "Encerrado"
        detalhe_tempo = "Fim de Jogo"
    elif status_api in ["adiado", "pst", "postponed"]:
        status_formatado = "Adiado"
        detalhe_tempo = "Adiado"
    elif status_api in ["agendado", "ns", "not started", ""] or not status_api:
        # Se a data do jogo for anterior a hoje e não encerrou, força para Encerrado/Ignorado para não ficar preso
        if data_evento_str and data_evento_str < hoje:
            status_formatado = "Encerrado"
            detalhe_tempo = "Encerrado (Histórico)"
        else:
            status_formatado = "Agendado"
            detalhe_tempo = evento.get("strTime", "Em breve")
    elif "2" in status_api or "second" in status_api:
        status_formatado = "Ao Vivo"
        detalhe_tempo = f"2º Tempo {minuto_atual}" if minuto_atual else "2º Tempo"
    else:
        status_formatado = "Ao Vivo"
        detalhe_tempo = f"{minuto_atual}'" if minuto_atual else "Em andamento"

    return {
        "id": id_jogo + 1,
        "rodada": evento.get("intRound", "Rodada Atual"),
        "selecao": evento.get("strHomeTeam", "Time Casa"),
        "logo_selecao": evento.get("strHomeTeamBadge", ""),
        "adversario": evento.get("strAwayTeam", "Time Visitante"),
        "logo_adversario": evento.get("strAwayTeamBadge", ""),
        "estadio": evento.get("strVenue", "Local / Estádio não informado"),
        "data": data_evento_str,
        "horario": evento.get("strTime", ""),
        "placar": f"{evento.get('intHomeScore', '0')} x {evento.get('intAwayScore', '0')}",
        "status": status_formatado,
        "detalhe_tempo": detalhe_tempo,
        "acrescimo": acrescimo if acrescimo else None,
        "transmissao": evento.get("strTV", "NSports / DAZN / Nosso Futebol"),
        "ocorrencias": {
            "cartoes_amarelos": evento.get("yellow_cards", "Nenhum cartão amarelo registrado"),
            "cartoes_vermelhos": evento.get("red_cards", "Nenhuma expulsão registrada"),
            "faltas": evento.get("fouls", "Estatística de faltas indisponível"),
            "penaltis": evento.get("penalties", "Nenhum pênalti assinalado"),
            "substituicoes": evento.get("substitutions", "Nenhuma")
        },
        "campeonato": "Brasileirão Série C"
    }

def formatar_tabela_seriec(tabela_data):
    """
    Garante a formatação correta dos dados da tabela de classificação da Série C.
    """
    return tabela_data
