import telebot
import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime


fansScreamsOptions = ["VAMOS, PANTERA! 🐆💪", "É a SUPER FÚRIA rapá!!! Exxxquece!!", "É HOJE, PANTERA! 🔥"]

# Bot token
bot = telebot.TeleBot("7665752409:AAFrH0NqlH2kjZg0N2XzGK-SOyLfYVR5esw")

# /start and /help commands
@bot.message_handler(commands=["start", "help"])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, "Chega maisss!! Bem vindo(a) ao FURIA CLUTCH, o bot dos fãs exclusivo da SUPER FURIA! 🐆\n"
                      "Em que podemos te ajudar meu furioso?:\n"
                      "/noticias - Últimas notícias da FURIA\n"
                      "/proximaspartidas - Próximos jogos do time\n"
                      "/ultimaspartidas - Resultados das últimas partidas\n"
                      "/jogadores - Conheça o elenco de CS\n"
                      "/torcida - Grito de guerra da nação FURIA!")

# /news command
@bot.message_handler(commands=["noticias"])
def noticias(msg: telebot.types.Message):
    bot.reply_to(msg, "📰 Notícia quentinha pros furiosos! 🐆\n"
                      "Confira os posts mais recentes da FURIA:\n"
                      "- X: https://x.com/FURIA\n"
                      "- Instagram: https://www.instagram.com/furia/\n"
                      "Bora ficar por dentro de tudo, pantera?")

# /next match command
@bot.message_handler(commands=["proximaspartidas"])
def partidas(msg: telebot.types.Message):
    try:
        url = "https://www.hltv.org/matches"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        upcoming_matches = soup.select('div.upcomingMatch')
        furia_match = None
        for match in upcoming_matches:
            teams = match.select('.matchTeams')
            if teams and 'FURIA' in teams[0].text:
                furia_match = match
                break

        if furia_match:
            opponent = furia_match.select_one('.matchTeams').text.strip().replace('FURIA', '').replace('vs', '').strip()
            date_time = furia_match.select_one('.matchTime').text.strip()
            event = furia_match.select_one('.matchEvent').text.strip() if furia_match.select_one('.matchEvent') else "Evento não especificado"

            reply = (f"🏆 Próxima partida da SUPER FURIA:\n"
                     f"Contra: {opponent}\n"
                     f"Data/Hora: {date_time}\n"
                     f"Evento: {event}\n"
                     f"🐆 Bora torcer, pantera?!")
            bot.reply_to(msg, reply)
        else:
            bot.reply_to(msg, "Nenhuma partida agendada encontrada pros furiosos! 🐆 Fique ligado nas redes da SUPER FURIA:\n"
                              "- X: https://x.com/FURIA\n"
                              "- Instagram: https://www.instagram.com/furiagg/")
    except Exception as e:
        bot.reply_to(msg, "Nenhuma partida agendada encontrada pros furiosos! 🐆 Fique ligado nas redes da SUPER FURIA:\n"
                          "- X: https://x.com/FURIA\n"
                          "- Instagram: https://www.instagram.com/furiagg/")

# /lastmatches command
@bot.message_handler(commands=["ultimaspartidas"])
def ultimas_partidas(msg: telebot.types.Message):
    opponent = "M80"
    result = "1-2"
    date_formatted = "22/03/2025"

    reply = (f"🏆 Última partida da SUPER FURIA:\n"
             f"Contra: {opponent}\n"
             f"Resultado: {result}\n"
             f"Data: {date_formatted}\n"
             f"🐆 Vamos com tudo na próxima, pantera!")
    bot.reply_to(msg, reply)

# /players command
@bot.message_handler(commands=["jogadores"])
def jogadores(msg: telebot.types.Message):
    bot.reply_to(msg, "👨‍🚀 Elenco da SUPER FURIA CS:\n"
                      "- KSCERATO: O rei da mira\n"
                      "- yuurih: Clutch machine\n"
                      "- FalleN: O professor e IGL\n"
                      "- chelo: O monstro do rifler\n"
                      "Quem é seu favorito? 😎")




# /fans command
@bot.message_handler(commands=["torcida"])
def torcida(msg: telebot.types.Message):
    bot.reply_to(msg, random.choice(fansScreamsOptions))

# Start the bot
bot.infinity_polling()