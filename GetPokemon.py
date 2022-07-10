import requests
from create_image import CreateImage


class GetPokemon:
    def __init__(self, name) -> None:
        self.name = name
        self.no_found = None

        self.request = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{self.name}'
            )

        self.status_200_or_400()

    def status_200_or_400(self):
        if self.request.status_code == 200:
            self.no_found = False
            self.response = self.request.json()
            self.get_pokemon_name()
            self.get_pokemon_image()
        else:
            self.no_found = True

    def get_pokemon_name(self):
        name_pokemon = self.response['forms'][0]['name']
        return f'{name_pokemon}!'

    def get_pokemon_image(self):
        image_pokemon_url = \
            self.response['sprites']['other']['home']['front_default']

        self.image_content = requests.get(image_pokemon_url).content

        file = CreateImage().create_image(self.image_content)
        return file
