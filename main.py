import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Automação de Notícias",
    description="Busca notícias em tempo real sobre qualquer tema para integração em Dashboards ou Bots."
)

# O os.getenv busca a chave nas variáveis de ambiente (Railway)
# Se não encontrar nada, o valor será None por segurança
API_KEY = os.getenv("NEWS_API_KEY")

@app.get("/")
def home():
    """Rota raiz para verificar se a API está online."""
    return {
        "status": "Online",
        "mensagem": "API de Notícias pronta para uso. Use o endpoint /buscar-noticias",
        "autor": "Engenharia de Software - Projeto Renda Passiva"
    }

@app.get("/buscar-noticias")
def buscar(tema: str):
    """
    Busca notícias via NewsAPI. 
    Parâmetro 'tema': O assunto que você deseja pesquisar.
    """
    # 1. Verificação de Segurança
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API_KEY não configurada no servidor.")

    # 2. Configuração da Requisição
    # Buscamos em inglês (en) por padrão para ter mais volume para o mercado global
    url = f"https://newsapi.org/v2/everything?q={tema}&apiKey={API_KEY}&language=en&pageSize=10&sortBy=publishedAt"

    try:
        response = requests.get(url)
        dados = response.json()

        # 3. Tratamento de Erro da NewsAPI
        if response.status_code != 200:
            return {"erro": "Falha na NewsAPI", "detalhe": dados.get("message", "Erro desconhecido")}

        # 4. Formatação dos dados para o cliente (JSON Limpo)
        noticias_limpas = []
        for art in dados.get("articles", []):
            noticias_limpas.append({
                "titulo": art.get("title"),
                "fonte": art.get("source", {}).get("name"),
                "data_publicacao": art.get("publishedAt"),
                "url": art.get("url"),
                "resumo": art.get("description")
            })

        return {
            "tema_buscado": tema,
            "total_resultados": len(noticias_limpas),
            "noticias": noticias_limpas
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no servidor: {str(e)}")