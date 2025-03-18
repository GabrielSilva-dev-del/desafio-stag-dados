import os
import pandas as pd
import json
import time
import google.generativeai as genai
import google.api_core.exceptions
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Verificar se a chave de API está definida
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("A variável de ambiente GEMINI_API_KEY não está definida.")

# Configurar a API do Google Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-1.5-pro')

def extrair_dados(texto, tentativas=3):
    """
    Função para extrair nome, email, telefone, interesse e orçamento do texto.
    Utiliza a API do Google Gemini para gerar as informações estruturadas.
    """
    prompt = f"""
    Extraia as seguintes informações do texto fornecido e retorne um objeto JSON com as chaves "nome", "email", "telefone", "interesses" e "orcamento". Se alguma informação não estiver presente, a chave correspondente deve ter o valor null.

    Texto:
    {texto}

    Formato de saída (JSON):
    {{
      "nome": "...",
      "email": "...",
      "telefone": "...",
      "interesses": "...",
      "orcamento": "..."
    }}
    """

    try:
        response = model.generate_content(prompt)
        dados = response.text.strip()

        # Remover blocos de código, se presentes
        if dados.startswith("```json"):
            dados = dados[7:-3].strip()

        # Verificar se a resposta segue o formato JSON
        try:
            dados_json = json.loads(dados)
            return {
                "nome": dados_json.get("nome"),
                "email": dados_json.get("email"),
                "telefone": dados_json.get("telefone"),
                "interesses": dados_json.get("interesses"),
                "orcamento": dados_json.get("orcamento")
            }
        except json.JSONDecodeError:
            print(f"Erro: A resposta não é um JSON válido. Resposta: {dados}")
            return None

    except google.api_core.exceptions.ResourceExhausted as e:
        if tentativas > 0:
            print(f"Erro ao processar a API: {e}. Tentando novamente em 20 segundos...")
            time.sleep(20)  # Espera 20 segundos e tenta novamente
            return extrair_dados(texto, tentativas - 1)  # Recursividade, tenta novamente.
        else:
            print(f"Erro ao processar a API: {e}. Limite de tentativas excedido.")
            return None
    except Exception as e:
        print(f"Erro ao processar a API: {e}")
        return None

def processar_csv(caminho_arquivo):
    """
    Função para ler o arquivo CSV e processar as conversas para extrair os dados.
    """
    try:
        df = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return []

    resultados = []

    for _, row in df.iterrows():
        texto = row['conversa']
        dados_extraidos = extrair_dados(texto)

        if dados_extraidos:
            resultados.append(dados_extraidos)
        else:
            print(f"Não foi possível extrair dados da linha: {row['id']}")

        time.sleep(5)  # Aumenta o atraso para 5 segundos

    return resultados

if __name__ == "__main__":
    caminho_arquivo = os.path.join("dados", "conversas_leads.csv")
    resultados = processar_csv(caminho_arquivo)

    if resultados:
        print("Resultados extraídos:")
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, Email: {resultado['email']}, Interesses: {resultado['interesses']}, Orçamento: {resultado['orcamento']}")
    else:
        print("Nenhum dado extraído ou houve erro ao processar as conversas.")