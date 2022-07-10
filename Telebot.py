import telebot
from messages import Hello_message, help_message, pokemon_no_found
from messages import github_message, commands_message
from GetPokemon import GetPokemon
from utils import slipt_message



class Telegram(telebot.TeleBot):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.bot = telebot.TeleBot(
            '5437930749:AAHC_uWRhVqw6-3Bk7-Et7FvFl4iofbwInc')

        self.configure()
        self.bot.infinity_polling()

    def configure(self):
        @self.bot.message_handler(commands=['start'])
        def send_wellcome(message):
            self.bot.reply_to(
                message,
                Hello_message)

        @self.bot.message_handler(commands=['help'])
        def send_help(message):
            self.bot.reply_to(
                message,
                help_message)

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
            pokemon = slipt_message(message)

            if GetPokemon().status_200_or_400(pokemon):
                name_pokemon = GetPokemon().get_pokemon_name(pokemon)
                GetPokemon().get_pokemon_image(name_pokemon)
                photo = open('pokemon.png', 'rb')
                self.bot.send_photo(
                    message.chat.id,
                    photo,
                    reply_to_message_id=message.id,
                    caption=f'{name_pokemon}!'
                )
            else:
                image = open('no_found.png', 'rb')
                self.bot.send_photo(
                    message.chat.id,
                    image,
                    caption=pokemon_no_found
                )

        @self.bot.message_handler(commands=['ability'])
        def send_stats_pokemon(message):
            pokemon = slipt_message(message)
            if GetPokemon().status_200_or_400(pokemon):
                name_pokemon = GetPokemon().get_pokemon_name(pokemon).title()
                ability = GetPokemon().get_pokemon_ability(pokemon)
                ability_list = ability.replace(' ', ' | ')
                self.bot.reply_to(
                    message,
                    f'{name_pokemon}: {ability_list}'
                )
            else:
                photo = open('no_found.png', 'rb')
                self.bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=pokemon_no_found
                )


Telegram()
