from flask import jsonify
from app import app, auth, cache
from app.services.scraping_service import get_producao_data, get_processamento_data, get_comercializacao_data, get_importacao_data, get_exportacao_data

@app.route('/')
@auth.login_required
@cache.cached()
def home():
    return "Desafio FIAP"

@app.route('/api/producao', methods=['GET'])
@auth.login_required
@cache.cached(timeout=86400)
def producao():

    """
    Endpoint para obter os dados de produção.
    ---
    tags:
      - Produção
    responses:
      200:
        description: Dados de produção retornados com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  Produto:
                    type: string
                  Quantidade:
                    type: string
      500:
        description: Erro ao obter os dados de produção
    """

    df = get_producao_data()
    if df is None:
        return jsonify({"error": "Falha ao obter os dados."}), 500

    # Converte o DataFrame para JSON
    return df.to_json(orient='records', force_ascii=False), 200

@app.route('/api/processamento', methods=['GET'])
@auth.login_required
@cache.cached(timeout=86400)
def processamento():

    """
    Endpoint para obter os dados de Processamento.
    ---
    tags:
      - Processamento
    responses:
      200:
        description: Dados de Processamento retornados com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  Cultivar:
                    type: string
                  Quantidade:
                    type: string
      500:
        description: Erro ao obter os dados de Processamento
    """

    df = get_processamento_data()
    if df is None:
        return jsonify({"error": "Falha ao obter os dados."}), 500

    # Converte o DataFrame para JSON
    return df.to_json(orient='records', force_ascii=False), 200

@app.route('/api/comercializacao', methods=['GET'])
@auth.login_required
@cache.cached(timeout=86400)
def comercializacao():

    """
    Endpoint para obter os dados de comercialização.
    ---
    tags:
      - Comercialização
    responses:
      200:
        description: Dados de Comercialização retornados com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  Produto:
                    type: string
                  Quantidade:
                    type: string
      500:
        description: Erro ao obter os dados de Comercialização
    """

    df = get_comercializacao_data()
    if df is None:
        return jsonify({"error": "Falha ao obter os dados."}), 500

    # Converte o DataFrame para JSON
    return df.to_json(orient='records', force_ascii=False), 200

@app.route('/api/importacao', methods=['GET'])
@auth.login_required
@cache.cached(timeout=86400)
def importacao():

    """
    Endpoint para obter os dados de importação.
    ---
    tags:
      - Importação
    responses:
      200:
        description: Dados de Importação retornados com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  Paises:
                    type: string
                  Quantidade:
                    type: string
                  Valor:
                    type: string
      500:
        description: Erro ao obter os dados de Importação
    """

    df = get_importacao_data()
    if df is None:
        return jsonify({"error": "Falha ao obter os dados."}), 500

    # Converte o DataFrame para JSON
    return df.to_json(orient='records', force_ascii=False), 200

@app.route('/api/exportacao', methods=['GET'])
@auth.login_required
@cache.cached(timeout=86400)
def exportacao():

    """
    Endpoint para obter os dados de Exportação.
    ---
    tags:
      - Exportação
    responses:
      200:
        description: Dados de Exportação retornados com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  Paises:
                    type: string
                  Quantidade:
                    type: string
                  Valor:
                    type: string
      500:
        description: Erro ao obter os dados de Exportação
    """

    df = get_exportacao_data()
    if df is None:
        return jsonify({"error": "Falha ao obter os dados."}), 500

    # Converte o DataFrame para JSON
    return df.to_json(orient='records', force_ascii=False), 200
