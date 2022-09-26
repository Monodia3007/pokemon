class Trainer:
    def __init__(self, nom,
                 pokemons=None):
        self.nom = nom
        self.pokemons = pokemons

    def __str__(self):
        return self.nom, self.pokemons

    def return_pokemons(self):
        """
        * paramètres : Le dresseur
        * valeur retournée : Les Pokémon attribué au dresseur
        """
        for pokemon in self.pokemons:
            print(pokemon.nom)

    def team_ko(self):
        """
        * paramètres : Le dresseur
        * valeur retournée : un booléen si la team est KO ou non

        """
        ko = True
        for pokemon in self.pokemons:
            if not pokemon.etre_ko():
                ko = False
        return ko

    def pokemon_standing(self):
        """
        * paramètres : Le dresseur
        * valeur retournée : indice d'un des pokemons encore en vie
        """
        for i in range(len(self.pokemons)):
            if not self.pokemons[i].etre_ko():
                fighting_pokemon = i
                return fighting_pokemon
