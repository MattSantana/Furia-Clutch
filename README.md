# FURIA CLUTCH - Um Bot de Telegram pra Fãs da FURIA

Falaaaaaaa avaliador, beleza? Aqui é o Matheus! 👋  
Criei esse bot pro Challenge 1 do processo técnico da FURIA, e ele foi feito pra ajudar os fãs a acompanharem o time de um jeito bem prático direto no Telegram.  
O **FURIA CLUTCH** é um bot que responde a comandos com infos do time, como próximas partidas, últimas partidas, elenco e até um grito de torcida pra animar os furiosos.  
Vou te explicar tudo de forma clara e organizada pra você entender direitinho como ele funciona. **Bora?** 🚀

---

## 📌 O que o Bot Faz?

O **FURIA CLUTCH** é um bot de Telegram que oferece as seguintes funções:

### 🤖 Comandos Interativos

O bot responde a comandos que os fãs podem usar pra interagir com ele:

- `/start` e `/ajuda`: Mostra uma mensagem de boas-vindas e a lista de comandos disponíveis.  
- `/noticias`: Fornece links pras redes sociais da FURIA (X e Instagram) pra conferir os posts mais recentes.  
- `/proximaspartidas`: Busca a próxima partida da FURIA no site HLTV.org e mostra detalhes como adversário, data/hora e evento.  
- `/ultimaspartidas`: Exibe informações sobre a última partida da FURIA (no momento, os dados são fixos no código).  
- `/jogadores`: Lista o elenco atual do time de CS:GO da FURIA, com os nicknames e uma breve descrição de cada jogador.  
- `/torcida`: Envia um grito de guerra aleatório pra animar os fãs (ex.: "VAMOS, PANTERA! 🐆💪").

---

## 📢 Informações do Time FURIA

O bot foi criado pra ajudar os fãs a ficarem por dentro do que tá rolando com o time FURIA, especialmente em esports como CS:GO.  
Ele entrega infos rápidas e úteis direto no chat do Telegram, além de animar a torcida com mensagens empolgantes.

---

## ⚙️ Como o Bot Funciona?

O **FURIA CLUTCH** foi desenvolvido em **Python** usando a biblioteca `python-telegram-bot` pra interagir com a API do Telegram.  
Ele faz **web scraping** no site **HLTV.org** pra buscar próximas partidas e responde a comandos enviados pelos usuários no Telegram.

**Fluxo de uso:**

1. O usuário adiciona o bot no Telegram (o bot já tá configurado com o token no código).  
2. O usuário envia comandos como `/start` ou `/proximaspartidas` no chat.  
3. O bot processa o comando (buscando dados se necessário) e responde com as informações no chat.

---

## 🧪 Como Executar o Bot?

### 1. Pré-requisitos

Antes de executar o bot, é necessário ter os seguintes itens instalados:  

- **Python 3.8 ou superior**: Para executar o código.  
- **Dependências do Python**: Instale as bibliotecas necessárias com o comando:

  ```bash
  pip install python-telegram-bot requests beautifulsoup4
### 🔐 Token do Bot:

O bot já está configurado com o token `7665752409:AAFrH0NqlH2kjZg0N2XzGK-SOyLfYVR5esw` no arquivo `main.py`.  
Você pode usar esse token pra testar o bot diretamente.  
No Telegram, procure pelo bot chamado **@challengeFuriaClutchBot** e comece a interagir com ele.

---

## 2. ⚙️ Configuração do Projeto

- Faça o download ou clone o projeto para o seu computador.  
- Na pasta do projeto, você encontrará:
  - `main.py`: O código principal do bot.

---

## 3. 🚀 Execução do Bot

- Abra o terminal na pasta do projeto.  
- Inicie o bot com o comando:

  ```bash
  python main.py
No Telegram, procure pelo bot chamado **@challengeFuriaClutchBot** e comece a interagir com ele enviando comandos como `/start`.

---

## 4. 💬 Utilização do Bot

- Envie comandos como `/proximaspartidas` ou `/jogadores` no chat do Telegram.  
- O bot vai responder com as informações diretamente no chat.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Para o desenvolvimento do bot.  
- **python-telegram-bot**: Biblioteca usada pra interagir com a API do Telegram.  
- **requests** e **BeautifulSoup**: Para fazer web scraping no site HLTV.org e buscar próximas partidas.

---

## ⚠️ Limitações

- Os dados da última partida (comando `/ultimaspartidas`) são **fixos no código** (hardcoded), ou seja, **não são atualizados em tempo real**.  
- O **web scraping** no HLTV.org pode falhar se o site mudar sua estrutura ou bloquear requisições.  
- O bot é **simples** e não possui funcionalidades como **notificações automáticas** ou interações mais dinâmicas.

---

## 🌟 Possíveis Melhorias

- **Integrar uma API de esports** (como a do HLTV ou outra) para buscar resultados de partidas **em tempo real**, evitando web scraping e dados fixos.  
- Adicionar **notificações automáticas**, para avisar os fãs sobre novas partidas, resultados ou eventos da FURIA.  
- **Expandir os comandos**, incluindo mais funcionalidades como:
  - Estatísticas dos jogadores.  
  - Agenda completa dos torneios.  
  - Comando para exibir **highlights** de partidas recentes.  
- Criar um **sistema de lembretes**, permitindo que os fãs solicitem notificações sobre partidas futuras diretamente no Telegram.

