import telebot
import botKey
import unidecode

bot = telebot.TeleBot(botKey.KEY)
answers = ["aquario", "aquarius"]

def decode(message):
	return unidecode.unidecode(message).lower()

def check(message):
	msg = decode(message)
	for answer in answers:
		if answer in msg:
			return True		
	return False

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Olá! Qual é a resposta?')
	
@bot.message_handler(func=lambda m: True)
def check_answer(message):
	if check(message.text):
		bot.send_message(message.chat.id, 'Acertou!')
	else:
		bot.send_message(message.chat.id, 'Errou!')
		

bot.polling()