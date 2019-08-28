###
### Author: Mikaeri Ohana
### Date: 8/27/2019
###

import crawler
import sys
import emoji
import telebot

token = sys.argv[1]
  
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, emoji.emojize("Hi! Welcome to the Crawler Bot! \nTell me the topics you like the most and I'll search it on Reddit and bring information to you! \n\n>>Just type '/NadaPraFazer topic_one' \nExample: /NadaPraFazer cats \n\nAND SEE THE MAGIC! :crystal_ball: \n\nWant to see more topics at the same time?\nType with semicolon! \nExample: /NadaPraFazer cats;dogs;turtles"))

@bot.message_handler(commands=['NadaPraFazer'])
def send_data(message):
    subreddits = str(message.text.split(" ")[1])
    try:
        answer = crawler.crawl(subreddits)
    except:
        answer = emoji.emojize("Something has happened. Our friends are working on it. We'll be right back! :thumbs_up: ")
   
    bot.reply_to(message, answer)

bot.polling()