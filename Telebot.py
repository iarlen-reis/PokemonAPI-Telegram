import telebot
from messages import Hello_message, help_message, pokemon_no_found
from messages import github_message, commands_message
from GetPokemon import GetPokemon


class Telegram(telebot.TeleBot):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.bot = telebot.TeleBot(
            'YOUR TOKEN')
        self.configure()
        self.bot.infinity_polling()

    def configure(self):
        @self.bot.message_handler(commands=['start'])
        def send_wellcome(message):
            self.bot.reply_to(
                message, Hello_message)

        @self.bot.message_handler(commands=['help'])
        def send_help(message):
            self.bot.reply_to(
                message, help_message)

        @self.bot.message_handler(commands=['github'])
        def send_github(message):
            self.bot.reply_to(
                message,
                github_message
            )

        @self.bot.message_handler(commands=['commands'])
        def send_commands(message):
            self.bot.reply_to(
                message,
                commands_message
            )

        @self.bot.message_handler(commands=['name'])
        def reply_message(message):
            self.pokemon = self.slipt_message(message)

            if not GetPokemon(self.pokemon).no_found:
                photo = open('pokemon.png', 'rb')
                self.bot.send_photo(
                    message.chat.id,
                    photo,
                    reply_to_message_id=message.id,
                    caption=GetPokemon(self.pokemon).get_pokemon_name()
                )
            else:
                image = open('no_found.png', 'rb')
                self.bot.send_photo(
                    message.chat.id,
                    image,
                    caption=pokemon_no_found
                )

    def slipt_message(self, message):
        context = ''.join(message.text)
        new_context = context.split(' ')
        final_context = new_context[1]
        return final_context


Telegram()
