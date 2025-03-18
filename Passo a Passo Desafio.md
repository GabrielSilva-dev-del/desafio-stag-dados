Inicialmente foi criado um repositorio no github e preparado um ambiente virtual pyhton para realização do projeto.

Na pasta do projeto foi executado python-m venv venv e foi ativado o ambiente virtual a partir do comando sourcevenv/bin/activate.

Foram instaladas as bibliotecas google-generativeai, pyhton-dotenv e pandas na pasta requirements.txtpip.

Apos tais passos foi obtida a API-KEY do google gemini a partir das orientações dadas no descritivo do desafio e foi feito o gerenciamento da chave a partir do arquivo .env .

Foi carregado a chave API no codigo utilizando a biblioteca python-dotenv e foi criado o arquivo .gitgnore para a segurança da chave no codigo, de modo que ela foi usada indiretamente.

Foi utilizada a biblioteca pandas para ler o arquivo conversas_leads.csv da pasta dados e foi criado uma função que recebe um texto de uma conversa e utiliza a API gemini para extrair as informações de interesse(nome, e-mail, telefone, interesse e orçamento).

Foi utlizado um loop para processar cada conversa e armazenar os resutados.

O codigo não funcionou como desejado devido ao erro 429 que se refere ao limite de quota da API, foram feitas varias modificações para a eliminação desse erro, porem o modelo escolhido gemini 1.5-pro por mais que esteja como ilimitado nas orientações do google, ainda assim apresentou esse erro.  Diante do exposto, esse foi o maior desafio do teste e se deu devido a problemas de conexão, sobrecarga da API devido ao grande volume de dados e sobrecarga da plataforma utilizada.