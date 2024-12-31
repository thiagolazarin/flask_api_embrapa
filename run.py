from app import app
from init_data import main as run_scraping

def start_flask_server():
    print("Iniciando servidor Flask...")
    app.run(host="0.0.0.0", port=5000)  # Certifique-se de usar estas configurações para o Vercel

if __name__ == "__main__":
    # Passo 1: Executar o init_data.py (garantir que isso só rode na primeira inicialização)
    print("Executando scraping e inicializando dados...")
    try:
        run_scraping()
        print("Scraping concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o scraping: {str(e)}")

    # Passo 2: Iniciar o servidor Flask
    start_flask_server()
