from utils import *


def affiche_marchants(dataset):
    """Affiche la liste des marchnats"""
    i = 1
    for marchant_name in dataset:
        print(f'{i}. {marchant_name.capitalize()}') # marchant_name.capitalise() -> met en majuscule la premiere lettre de chaque nom de marchant
        i += 1
    
def recup_option():
    """Recupere l'option choisie pour un menu"""
    return int(input('Selectionnez une option: '))

affiche_marchants(MARCHANTS)
option_choix_marchant = recup_option()

marketers_name = marketers[option_choix_marchant]
for article in MARCHANTS[marketers_name.lower()]:
        print(f"{article} -> {MARCHANTS[marketers_name.lower()][article]['price']}$/{MARCHANTS[marketers_name.lower()][article]['unite']}")
