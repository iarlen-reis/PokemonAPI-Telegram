from utils import list_to_string


def get_stats_abilitys(requets):
    response = requets
    all_ability = []
    for num in range(0, 2):
        stats_1 = response['abilities'][num]['ability']['name']
        all_ability.append(stats_1)
    ability = list_to_string(all_ability)

    return ability
