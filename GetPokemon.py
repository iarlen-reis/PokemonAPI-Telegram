import requests
from utils import CreateImage
from ability_pokemon import get_stats_abilitys


class GetPokemon:
    def status_200_or_400(self, pokemon):
        request = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        )
        if request.status_code == 200:
            return True
        else:
            return False

    def get_pokemon_name(self, pokemon):
        request = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        )
        if request.status_code == 200:
            self.no_found = False
            response = request.json()
            name_pokemon = response['forms'][0]['name']
            
        return name_pokemon

    def get_pokemon_image(self, pokemon):
        request = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        )
        if request.status_code == 200:
            self.no_found = False
            response = request.json()
        image_pokemon_url = \
            response['sprites']['other']['home']['front_default']

        self.image_content = requests.get(image_pokemon_url).content

        file = CreateImage().create_image(self.image_content)
        return file

    def get_pokemon_ability(self, pokemon):
        request = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        )
        if request.status_code == 200:
            self.no_found = False
            response = request.json()
            stats = get_stats_abilitys(response)
            return stats
        else:
            self.no_found = True
