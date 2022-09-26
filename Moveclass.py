from random import randint, choice
from typing import List, Any


class Moves:
    def __init__(self, nom="Missing Move",
                 typ=choice(["Water", "Flying", "Normal", "Fire", "Electric", "Ghost", "Poison", "Dragon", "Bug", "Ice",
                             "Psychic"]),
                 category=choice(["Physical", "Special"]),
                 pp=randint(1, 7) * 5,
                 power=randint(50, 150),
                 accuracy=randint(50, 100)):
        self.nom = nom
        self.type = typ
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy

    def __str__(self):
        return self.nom

    def type_advantage(self, target):
        """
        * paramètres : l'attaque et la cible
        * valeur retournée : le coefficient multiplicateur par rapport au type_table
        """
        if target.type[1] is not None:
            type_multiplicator = type_table[type_number[self.type]][type_number[target.type[0]]] * \
                                 type_table[type_number[self.type]][type_number[target.type[1]]]
        else:
            type_multiplicator = type_table[type_number[self.type]][type_number[target.type[0]]]
        if type_multiplicator < 1:
            print("Ceci n'est pas très efficace.")
        elif type_multiplicator > 1:
            print("Ceci est très efficace.")
        return type_multiplicator

    def damage(self, attacker, target):
        """
        * paramètres : l'attaque, le pokemon qui attaque et la cible
        * valeur retournée : Le nombre de pv retiré à la cible
        """
        if self.category == "Physical":
            dmg = ((((2 * 50) / 5 + 2) * self.power * (attacker.atk / target.defense)) / 50 + 2) * self.type_advantage(
                target)
        elif self.category == "Special":
            dmg = ((((2 * 50) / 5 + 2) * self.power * (
                    attacker.sp_attaque / target.sp_defense)) / 50 + 2) * self.type_advantage(target)
        else:
            dmg = 0
        return dmg


type_number = {"Normal": 0, "Fire": 1, "Water": 2, "Plant": 3, "Electric": 4, "Ice": 5, "Fighting": 6, "Poison": 7,
               "Ground": 8, "Flying": 9, "Psychic": 10, "Bug": 11, "Rock": 12, "Ghost": 13, "Dragon": 14,
               "Dark": 15}  # correspond aux indices de la type_table par rapport aux types
type_table = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1],
              [1, 0.5, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 0.5],
              [1, 2, 0.5, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 0.5],
              [1, 0.5, 2, 0.5, 1, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1],
              [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1],
              [1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1],
              [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2],
              [1, 1, 1, 2, 1, 1, 1, 0.5, 0.5, 1, 1, 2, 0.5, 0.5, 1, 1],
              [1, 2, 1, 0.5, 2, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1],
              [1, 1, 1, 2, 0.5, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0],
              [1, 0.5, 1, 2, 1, 1, 0.5, 2, 1, 0.5, 2, 1, 1, 0.5, 1, 2],
              [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0.5],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
              [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5]]  # table des avantages de types
