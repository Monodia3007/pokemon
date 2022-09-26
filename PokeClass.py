from random import randint, choice


class Pokemon:
    def __init__(self, nom: str = "MissingNo",
                 typ1=choice(
                     ["Water", "Flying", "Normal", "Fire", "Electric", "Ghost", "Poison", "Dragon", "Bug", "Ice",
                      "Psychic"]),
                 typ2=choice(
                     ["Water", "Flying", "Normal", "Fire", "Electric", "Ghost", "Poison", "Dragon", "Bug", "Ice",
                      "Psychic", None]),
                 vitesse=randint(1, 51),
                 attaque=randint(51, 100),
                 defense=randint(1, 50),
                 pv_max=randint(101, 150),
                 sp_attaque=randint(51, 100),
                 sp_defense=randint(1, 50),
                 moves=None):
        self.pvActuels = None
        self.nom = nom
        self.type = (typ1, typ2)
        self.vitesse = vitesse
        self.atk = attaque
        self.defense = defense
        self.sp_attaque = sp_attaque
        self.sp_defense = sp_defense
        self.pv_max = pv_max
        self.pv_actuels = pv_max
        self.moves = moves

    def __str__(self):
        print(self.nom, self.type, self.vitesse, self.attaque, self.defense, self.pvActuels, self.sp_attaque,
              self.sp_defense, self.moves)

    def etre_ko(self):
        """
        * paramètres : Le Pokémon
        * valeur retournée : Si le Pokémon est KO avec un booléen
        """
        return self.pv_actuels <= 0

    def attaque(self, move, target):
        """
        * paramètres : Le Pokémon, l'attaque et la cible
        * valeur retournée : N/A
        """
        if move is not None:
            if randint(0, 100) < move.accuracy:
                target.pv_actuels -= move.damage(self, target)
            else:
                print("L'attaque à raté LOL")

    def return_moves(self):
        move_number = 1
        '''
        * paramètres : Le Pokémon
        * valeur retournée : Les attaques attribué au Pokémon
        '''
        for move in self.moves:
            print(move_number, move)
            move_number += 1
