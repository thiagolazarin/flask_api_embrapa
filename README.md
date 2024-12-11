# My Flask API

Este é um projeto de API desenvolvido com Flask, que inclui operações web scraping e autenticação básica.

## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai dados de páginas web (título, cabeçalhos, parágrafos) usando BeautifulSoup.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
intro_api/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scraping_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── __init__.py
│   └── config.py
├── requirements.txt
├── Dockerfile
├── README.md
└── run.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por funcionalidades.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`Dockerfile`**: Configurações para Docker.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
gh repo clone thiagolazarin/flask_api_embrapa
cd flask_api_embrapa
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000`.

## 🐳 Como Usar com Docker

### 1. Construa a Imagem Docker

```bash
docker build -t api-desafio-fiap .
```

### 2. Execute o Container

```bash
docker run -p 5000:5000 api-desafio-fiap
```

Acesse a aplicação em `http://localhost:5000`.

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
