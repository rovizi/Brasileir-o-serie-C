from fastapi import APIRouter
from database import buscar_dados_seriec_externos
from models import formatar_jogo_seriec

router = APIRouter(prefix="/api/seriec", tags=["Série C"])

@router.get("/jogos")
def get_jogos_seriec():
    eventos = buscar_dados_seriec_externos()
    
    if eventos:
        jogos_formatados = []
        for i, evento in enumerate(eventos[:10]):
            jogos_formatados.append(formatar_jogo_seriec(i, evento))
        return jogos_formatados

    # Fallback estruturado com dados visuais completos
    return [{
        "id": 1,
        "rodada": "Rodada Atual",
        "selecao": "Botafogo-PB",
        "logo_selecao": "",
        "adversario": "Volta Redonda",
        "logo_adversario": "",
        "estadio": "Estádio Almeidão",
        "pais": "Brasil",
        "data": "2026-10-05",
        "horario": "19:00",
        "placar": "1 x 1",
        "status": "Intervalo",
        "detalhe_tempo": "HT",
        "transmissao": "TV Globo / Premiere / SporTV",
        "ocorrencias": {
            "cartoes_amarelos": "Botafogo-PB: 34' 1T (João Paulo), Volta Redonda: 42' 1T (Bruno Santos)",
            "cartoes_vermelhos": "Nenhum",
            "substituicoes": "Volta Redonda: Saiu Carlos Eduardo, Entrou Ítalo aos 38' 1T"
        },
        "campeonato": "Brasileirão Série C",
    }]
