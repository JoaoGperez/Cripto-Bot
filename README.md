# Cripto-Bot

Bot para consulta de preços de criptomoedas usando a API CoinGecko e integração com Twilio para envio de mensagens.

## 📖 Descrição

Este projeto foi desenvolvido para fornecer informações sobre preços de criptomoedas via WhatsApp usando a API CoinGecko e Twilio. Ele permite consultar preços atuais, visualizar histórico de consultas e exportar dados para CSV.

## 🚀 Funcionalidades

- Consultar o preço atual de uma criptomoeda.
- Consultar o histórico de preços de uma criptomoeda.
- Salvar consultas de preços no histórico do usuário.
- Exportar dados de preços para um arquivo CSV.

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- Twilio
- CoinGecko API
- dotenv
- Ngrok

## 📋 Pré-requisitos

- Python 3.9 ou superior.
- Conta no Twilio.
- Ngrok (para expor o servidor local).

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/JoaoGperez/Cripto-Bot.git
   cd seu-repositorio

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv\Scripts\activate
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Crie um arquivo [.env](http://_vscodecontentref_/1) na raiz do projeto e adicione suas credenciais do Twilio:

    ```env
    TWILIO_PHONE=seu_numero_twilio
    TWILIO_ACCOUNT_SID=seu_account_sid
    TWILIO_AUTH_TOKEN=seu_auth_token
    ```

## Uso

1. Execute o bot:

    ```sh
    python modules/bot.py
    ```

2. Envie mensagens para o número do Twilio configurado para interagir com o bot.

## Comandos Disponíveis

- `preço de [criptomoeda]`: Consulta o preço atual de uma criptomoeda (exemplo: `preço de bitcoin`).
- `histórico`: Exibe o histórico das consultas de preços.
- `salvar [criptomoeda]`: Salva uma criptomoeda no histórico (exemplo: `salvar bitcoin`).
- `exportar [criptomoeda]`: Exporta os dados de preços para um arquivo CSV.
- `ajuda`: Exibe os comandos disponíveis.