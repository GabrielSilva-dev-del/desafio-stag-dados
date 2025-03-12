# Desafio Técnico: Estágio em Ciência de Dados - Morada.ai

Este repositório contém as informações necessárias para o desafio técnico da vaga de Estágio em Ciência de Dados na Morada.ai.

## Sobre o Desafio

O desafio consiste em desenvolver uma aplicação que utilize Large Language Models (LLMs) através da API do Google Gemini para processar e analisar dados de forma criativa e eficiente. Você pode escolher entre três opções de projetos:

1. **Extrator de Informações de Conversas**: Desenvolva uma IA que extraia dados estruturados de conversas entre um assistente e um lead imobiliário.

2. **Assistente Virtual para Consulta de Empreendimentos**: Crie uma IA que responda perguntas sobre empreendimentos imobiliários disponíveis.

3. **Sua Própria Ideia**: Proponha e desenvolva sua própria aplicação utilizando LLMs no contexto imobiliário ou de atendimento ao cliente.

## Estrutura do Repositório

- `desafio-estagiario-cientista-dados.md`: Descrição completa do desafio técnico
- `dados/`: Pasta contendo os datasets necessários para o desafio
  - `empreendimentos.csv`: Dados de empreendimentos fictícios
  - `conversas_leads.csv`: Conversas fictícias entre assistentes e leads

## Como Começar

1. Leia atentamente o arquivo `desafio-estagiario-cientista-dados.md` para entender os requisitos e opções de projeto
2. Explore os dados fornecidos na pasta `dados/`
3. Escolha uma das opções de projeto ou proponha sua própria ideia
4. Crie um ambiente de desenvolvimento adequado para trabalhar com LLMs
5. Obtenha uma API key do Google Gemini através do [Google AI Studio](https://aistudio.google.com/)
6. Configure sua API key como variável de ambiente (não inclua a API key no código)
7. Desenvolva sua solução
8. Prepare a documentação e apresentação dos resultados

## Requisitos Obrigatórios

1. Utilizar a API do Google Gemini (é obrigatório o uso desta API específica)
2. Implementar um mecanismo seguro para gerenciar a API key (recomendamos o uso de variáveis de ambiente)
3. Utilizar os dados fornecidos na pasta "dados" do repositório
4. Implementar uma solução funcional que processe dados e extraia informações relevantes
5. Apresentar os resultados de forma organizada e visual
6. Documentar o código e a metodologia utilizada
7. **IMPORTANTE**: Não incluir sua API key no código ou em qualquer arquivo do repositório

## Recursos Úteis

- [Google AI Studio](https://aistudio.google.com/)
- [Tutorial da API do Google Gemini (Python)](https://ai.google.dev/gemini-api/docs/get-started/tutorial?hl=pt-br&lang=python)
- [Biblioteca Python para Google Gemini API](https://github.com/google/generative-ai-python)
- [Documentação do LangChain](https://python.langchain.com/docs/introduction/)

## Critérios de Avaliação

Os principais critérios de avaliação serão:
- Criatividade da solução implementada
- Estrutura e organização do código
- Apresentação da solução
- Eficácia no processamento das informações
- Clareza na documentação
- Segurança no tratamento de credenciais (API keys)

## Considerações Finais

Este projeto foi desenvolvido para simular um desafio real de processamento de linguagem natural no contexto imobiliário. A lógica foi otimizada para garantir a melhor experiência possível para os candidatos. Quaisquer dúvidas ou problemas, por favor, abra uma issue no repositório.

## Instruções para Envio

- Subir o código para um repositório no GitHub;
- Incluir um README.md no repositório contendo a documentação, quais foram os principais desafios, e uma instrução de como executar o projeto;
- Incluir instruções claras sobre como configurar a API key do Google Gemini para executar o projeto
- Enviar o link do repositório até o prazo determinado.

## Perguntas Frequentes

### Qual linguagem?

Não temos preferência por linguagem. Porém, aqui utilizamos: Python

### Devo construir uma interface?

Não é necessário desenvolver uma interface gráfica para este projeto. O foco principal da avaliação será a lógica aplicada e a robustez do código. Estamos interessados em verificar se o código está bem organizado, legível e se ele atende aos critérios estabelecidos pelos testes.

### Quando vou receber meu feedback?

Você receberá o feedback em até 15 dias após o encerramento das inscrições.

### Posso realizar alguma alteração depois do prazo de encerramento?

Não é possível realizar alterações após o prazo estabelecido. Mesmo que modificações sejam feitas após este prazo, nossa equipe avaliará apenas o último commit válido realizado antes do encerramento das inscrições.

### Posso usar outros frameworks além da API do Google Gemini?

Sim, você pode utilizar frameworks como LangChain que facilitam a implementação de aplicações com LLMs, desde que a API do Google Gemini seja a base da sua solução.

### Como devo gerenciar a API key do Google Gemini?

Recomendamos fortemente o uso de variáveis de ambiente para armazenar sua API key. Nunca inclua sua API key diretamente no código ou em arquivos que serão enviados ao repositório. No README do seu projeto, inclua instruções claras sobre como configurar a variável de ambiente necessária para executar o projeto.

Boa sorte!