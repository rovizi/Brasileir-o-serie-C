# API Série C - Live Goal ⚽

API desenvolvida em **FastAPI** para rastreamento de partidas da **Série C do Campeonato Brasileiro**, focada em fornecer dados em tempo real, placares, status de partidas e ocorrências detalhadas.

## 🚀 Funcionalidades
- **Status em Tempo Real**: Identificação automática se a partida está *Agendada*, *Ao Vivo*, em *Intervalo* (descanso) ou *Finalizada*.
- **Ocorrências da Partida**: Rastreamento detalhado de cartões amarelos, cartões vermelhos e substituições de jogadores.
- **Estrutura Simples**: Arquitetura modular limpa contendo apenas 4 arquivos principais na raiz (`main.py`, `database.py`, `models.py`, `jogos.py`).
- **Fallback de Segurança**: Mock estruturado para garantir estabilidade caso a API externa oscile.

## 📡 Endpoints Disponíveis

### 1. Raiz da API
- **URL:** `GET /`
- **Retorno:** Mensagem de status confirmando que a API está online.

### 2. Listagem de Jogos da Série C
- **URL:** `GET /api/seriec/jogos`
- **Retorno:** Retorna uma lista JSON com as partidas, placares, status dinâmicos e ocorrências.

## 🛠️ Exemplo de Resposta da API (`/api/seriec/jogos`)

```json
[
  {
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
    "campeonato": "Brasileirão Série C"
  }
]
