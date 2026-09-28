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

    # Fallback estruturado com os novos campos de cartões, substituições e intervalo
    return [{
        "id": 1,
        "selecao": "Botafogo-PB",
        "adversario": "Volta Redonda",
        "data": "2026-10-05",
        "horario": "19:00",
        "placar": "1 x 1",
        "status": "Intervalo",
        "detalhe_tempo": "HT",
        "ocorrencias": {
            "cartoes_amarelos": "Botafogo-PB: 34' 1T (João Paulo), Volta Redonda: 42' 1T (Bruno Santos)",
            "cartoes_vermelhos": "Nenhum",
            "substituicoes": "Volta Redonda: Saiu Carlos Eduardo, Entrou Ítalo aos 38' 1T"
        },
        "campeonato": "Brasileirão Série C",
    }]