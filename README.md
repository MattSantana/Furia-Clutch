# FURIA CLUTCH - Um Bot de Telegram pra Fãs da FURIA

Falaaaaaaa avaliador, beleza? Aqui é o Matheus! 👋 Criei esse bot pro Challenge 1 do processo técnico da FURIA, e ele foi feito pra ajudar os fãs a acompanharem o time de um jeito bem prático direto no Telegram.  
O **FURIA CLUTCH** é um bot que responde a comandos com infos do time, como próximas partidas, últimas partidas, elenco e até um grito de torcida pra animar os furiosos.  
Vou te explicar tudo de forma clara e organizada pra você entender direitinho como ele funciona. Bora? 🚀

## O que o Bot Faz?

O **FURIA CLUTCH** é um bot de Telegram que oferece as seguintes funções:

### 🤖 Comandos Interativos

O bot responde a comandos que os fãs podem usar pra interagir com ele:

- `/start` e `/ajuda`: Mostra uma mensagem de boas-vindas e a lista de comandos disponíveis.  
- `/noticias`: Fornece links pras redes sociais da FURIA (X e Instagram) pra conferir os posts mais recentes.  
- `/proximaspartidas`: Busca a próxima partida da FURIA no site HLTV.org e mostra detalhes como adversário, data/hora e evento.  
- `/ultimaspartidas`: Exibe informações sobre a última partida da FURIA (no momento, os dados são fixos no código).  
- `/jogadores`: Lista o elenco atual do time de CS:GO da FURIA, com os nicknames e uma breve descrição de cada jogador.  
- `/torcida`: Envia um grito de guerra aleatório pra animar os fãs (ex.: "VAMOS, PANTERA! 🐆💪").

### 📢 Informações do Time FURIA

O bot foi criado pra ajudar os fãs a ficarem por dentro do que tá rolando com o time FURIA, especialmente em esports como CS:GO.  
Ele entrega infos rápidas e úteis direto no chat do Telegram, além de animar a torcida com mensagens empolgantes.

## Como o Bot Funciona?

O **FURIA CLUTCH** foi desenvolvido em Python usando a biblioteca `python-telegram-bot` pra interagir com a API do Telegram.  
Ele faz web scraping no site HLTV.org pra buscar próximas partidas e responde a comandos enviados pelos usuários no Telegram.

O fluxo de uso é o seguinte:

- O usuário adiciona o bot no Telegram (o bot já tá configurado com o token no código).  
- O usuário envia comandos como `/start` ou `/proximaspartidas` no chat.  
- O bot processa o comando (buscando dados se necessário) e responde com as informações no chat.

## Como Executar o Bot?

### 1. Pré-requisitos

Antes de executar o bot, é necessário ter os seguintes itens instalados:

- **Python 3.8 ou superior**: Para executar o código.  
- **Dependências do Python**: Instale as bibliotecas necessárias com o seguinte comando:

```bash
pip install python-telegram-bot requests beautifulsoup4
