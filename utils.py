"""
Module qui définit l'ensemble des variables du pogramme
"""

MARCHANTS = {
    'maxi': {
        'patates': {'price': 5, 'unite': 'kg'},
        'tomates': {'price': 6, 'unite': 'kg'},
        'viandes': {'price': 30, 'unite': 'kg'},
        'papier': {'price': 20, 'unite': 'unite'},
        'poisson': {'price': 25, 'unite': 'kg'}
    },
    'rona': {
        'bois': {'price': 50, 'unite': 'unite'},
        'ceramique': {'price': 10, 'unite': 'unite'},
        'tondeuse': {'price': 500, 'unite': ''},
        'peinture': {'price': 80, 'unite': 'gallon'}
    },
    'epicier': {
        'lait': {'price': 5, 'unite': 'litre'},
        'biere': {'price': 20, 'unite': 'boite'},
        'cigarette': {'price': 15, 'unite': 'boite'},
        'essence': {'price': 2, 'unite': 'litre'}
    }
}

marketers = {
    1: 'maxi', 
    2: 'rona',    
    3: 'epicier'    
}
