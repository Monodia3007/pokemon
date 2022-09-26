from Pokeclass import Pokemon
from Moveclass import Moves
from TrainerClass import Trainer


def combattre(joueur1, joueur2):
    """
    * paramètres : 2 Dresseurs avec leurs équipes de Pokémon(s)
    * valeur retournée : Le nom du Pokémon et du dresseur gagnant
    """
    fighting_pokemon1 = 0
    fighting_pokemon2 = 0
    while True:
        fighting_pokemon1, selected_move1 = choix_action(joueur1, fighting_pokemon1)
        fighting_pokemon2, selected_move2 = choix_action(joueur2, fighting_pokemon2)
        if selected_move1 is not None and selected_move2 is not None:  # Vérifie si les 2 joueurs ont choisi l'attaque
            if joueur1.pokemons[fighting_pokemon1].vitesse < joueur2.pokemons[fighting_pokemon2].vitesse:  # Vérifie
                # quel pokemon est le plus rapide pour le faire attaquer en premier.
                joueur2.pokemons[fighting_pokemon2].attaque(joueur2.pokemons[fighting_pokemon2].moves[selected_move2],
                                                            joueur1.pokemons[fighting_pokemon1])  # Le Pokémon du
                # joueur 2 attaque le Pokémon du joueur 1
                print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
                print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
                if joueur1.pokemons[fighting_pokemon1].etre_ko():  # Vérifie si la team du joueur 1 est KO après la
                    # mort d'un de leur pokemon
                    if joueur1.team_ko():
                        print(winner + joueur2.nom)
                        break
                    else:
                        fighting_pokemon1 = joueur1.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO
                        # pour l'envoyer au combat
                joueur1.pokemons[fighting_pokemon1].attaque(joueur1.pokemons[fighting_pokemon1].moves[selected_move2],
                                                            joueur2.pokemons[fighting_pokemon2])
                # Le Pokémon du joueur 1 attaque le Pokémon du joueur 2
                print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
                print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
                if joueur2.pokemons[fighting_pokemon2].etre_ko():  # Vérifie si la team du joueur 2 est KO après la
                    # mort d'un de leur pokemon
                    if joueur2.team_ko():
                        print(winner + joueur1.nom)
                        break
                    else:
                        fighting_pokemon2 = joueur2.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO
                        # pour l'envoyer au combat
                selected_move1 = None
                selected_move2 = None
            else:
                joueur1.pokemons[fighting_pokemon1].attaque(joueur1.pokemons[fighting_pokemon1].moves[selected_move2],
                                                            joueur2.pokemons[fighting_pokemon2])
                # Le Pokémon du joueur 1 attaque le Pokémon du joueur 2
                print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
                print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
                if joueur2.pokemons[fighting_pokemon2].etre_ko():  # Vérifie si la team du joueur 2 est KO après la
                    # mort d'un de leur pokemon
                    if joueur2.team_ko():
                        print(winner + joueur1.nom)
                        break
                    else:
                        fighting_pokemon2 = joueur2.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO
                        # pour l'envoyer au combat
                joueur2.pokemons[fighting_pokemon2].attaque(joueur2.pokemons[fighting_pokemon2].moves[selected_move2],
                                                            joueur1.pokemons[fighting_pokemon1])
                # Le Pokémon du joueur 2 attaque le Pokémon du joueur 1
                print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
                print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
                if joueur1.pokemons[fighting_pokemon1].etre_ko():  # Vérifie si la team du joueur 1 est KO après la
                    # mort d'un de leur pokemon
                    if joueur1.team_ko():
                        print(winner + joueur2.nom)
                        break
                    else:
                        fighting_pokemon1 = joueur1.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO
                        # pour l'envoyer au combat
                selected_move1 = None
                selected_move2 = None
        if selected_move1 is not None and selected_move2 is None:  # Vérifie si le joueur 1 a choisi l'attaque et
            # l'autre non
            joueur1.pokemons[fighting_pokemon1].attaque(joueur1.pokemons[fighting_pokemon1].moves[selected_move1],
                                                        joueur2.pokemons[fighting_pokemon2])
            # Le Pokémon du joueur 1 attaque le Pokémon du joueur 2
            print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
            print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
            if joueur2.pokemons[fighting_pokemon2].etre_ko():  # Vérifie si la team du joueur 2 est KO après la mort
                # d'un de leur pokemon
                if joueur2.team_ko():
                    print(winner + joueur1.nom)
                    break
                else:
                    fighting_pokemon2 = joueur2.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO pour
                    # l'envoyer au combat
            selected_move1 = None
            selected_move2 = None
        if selected_move1 is None and selected_move2 is not None:  # Vérifie si le joueur 2 a choisi l'attaque et
            # l'autre non
            joueur2.pokemons[fighting_pokemon2].attaque(joueur2.pokemons[fighting_pokemon2].moves[selected_move2],
                                                        joueur1.pokemons[fighting_pokemon1])
            # Le Pokémon du joueur 2 attaque le Pokémon du joueur 1
            print(joueur2.pokemons[fighting_pokemon2].nom + " :", joueur2.pokemons[fighting_pokemon2].pv_actuels)
            print(joueur1.pokemons[fighting_pokemon1].nom + " :", joueur1.pokemons[fighting_pokemon1].pv_actuels)
            if joueur1.pokemons[fighting_pokemon1].etre_ko():  # Vérifie si la team du joueur 1 est KO après la mort
                # d'un de leur pokemon
                if joueur1.team_ko():
                    print(winner + joueur2.nom)
                    break
                else:
                    fighting_pokemon1 = joueur1.pokemon_standing()  # Vérifie quel pokemon n'est pas encore KO pour
                    # l'envoyer au combat
    if joueur1.team_ko():  # Vérifie si le pokemon du joueur 1 est KO puis renvoie le vainqueur
        return joueur2.pokemons[fighting_pokemon2].nom, joueur2.nom
    else:
        return joueur1.pokemons[fighting_pokemon1].nom, joueur1.nom


def choix_action(joueur, fighting_pokemon):
    print(separation)
    print("1-Attaque")
    print("2-Pokemon")
    print(separation)
    selected_action = int(
        input("Choisissez une action :"))  # Demande au joueur 1 s'il choisit d'attaquer ou de changer de pokemon
    assert (
            1 <= selected_action <= 2), "La valeur indiqué n'est pas valide. Il faut qu'elle soit entre 1 et 2"
    if selected_action == 1:
        selected_move = choix_attaque(joueur, fighting_pokemon)
    elif selected_action == 2:
        fighting_pokemon, selected_move = choix_pokemon(joueur)
    else:
        selected_move = 0
    return fighting_pokemon, selected_move


def choix_pokemon(joueur):
    selected_move = None
    print(separation)
    print(joueur.return_pokemons())
    print(separation)
    fighting_pokemon = int(input("Choisissez un pokemon :")) - 1  # Demande au joueur 1 quel Pokémon il veut
    assert (
            len(joueur.pokemons) > fighting_pokemon >= 0), "La valeur indiqué n'est pas valide." \
                                                           " Il faut qu'elle soit entre 1 et le nombre total de Pokémon"
    return fighting_pokemon, selected_move


def choix_attaque(joueur, fighting_pokemon):
    print(separation)
    print(joueur.pokemons[fighting_pokemon].return_moves())
    print(separation)
    selected_move = int(input("Choisissez une attaque :")) - 1  # Demande au joueur 1 quelle attaque il veut
    assert (len(joueur.pokemons[
                    fighting_pokemon].moves) > selected_move >= 0), "La valeur indiqué n'est pas valide." \
                                                                    " Il faut qu'elle soit entre 1 et le nombre total" \
                                                                    " d'attaque"
    return selected_move


def speed_comparison(joueur1, fighting_pokemon1, joueur2, fighting_pokemon2):
    if joueur1.pokemons[fighting_pokemon1].vitesse < joueur2.pokemons[fighting_pokemon2].vitesse:
        fastest_player = joueur2
        slowest_player = joueur1
    else:
        fastest_player = joueur1
        slowest_player = joueur2
    return fastest_player, slowest_player


scratch = Moves("Scratch", "Normal", "Physical", 35, 40, 100)
hyperbeam = Moves("Hyperbeam", "Normal", "Special", 5, 150, 90)
thunderbolt = Moves("Thunderbolt", "Electric", "Special", 15, 90, 100)
wild_charge = Moves("Wild Charge", "Electric", "Physical", 15, 90, 100)
focus_blast = Moves("Focus Blast", "Fighting", "Special", 5, 120, 70)
slam = Moves("Slam", "Normal", "Physical", 20, 80, 75)
fly = Moves("Fly", "Flying", "Physical", 15, 90, 95)
dragon_pulse = Moves("Dragon Pulse", "Dragon", "Special", 10, 85, 100)
flame_thrower = Moves("Flame Thrower", "Fire", "Special", 15, 90, 100)
ancient_power = Moves("Ancient Power", "Rock", "Special", 5, 60, 100)
last_resort = Moves("Last Resort", "Normal", "Physical", 5, 140, 100)
tackle = Moves("Tackle", "Normal", "Physical", 35, 40, 100)
double_edge = Moves("Double-Edge", "Normal", "Physical", 15, 120, 100)
bite = Moves("Bite", "Dark", "Physical", 25, 60, 100)

pikachu = Pokemon("Pikachu", "Electric", None, 156, 117, 90, 142, 112, 101,
                  [thunderbolt, wild_charge, focus_blast, slam])
charizard = Pokemon("Charizard", "Fire", "Flying", 167, 149, 143, 185, 177, 150,
                    [fly, dragon_pulse, flame_thrower, ancient_power])
eevee = Pokemon("Eevee", "Normal", None, 117, 117, 112, 162, 106, 128, [last_resort, tackle, double_edge, bite])
squirtle = Pokemon("Squirtle", "Water", None, 104, 110, 128, 151, 112, 127, )
gyarados = Pokemon("Gyarados", "Water", "Flying", 146, 194, 144, 202, 123, 167)
gengar = Pokemon("Gengar", "Ghost", "Poison", 178, 128, 123, 167, 200, 139)
articuno = Pokemon("Articuno", "Ice", "Flying", 150, 150, 167, 197, 161, 194)
mewtwo = Pokemon("Mewtwo", "Psychic", None, 200, 178, 156, 213, 226, 156, [Moves(), Moves(), Moves(), Moves()])
scyther = Pokemon("Scyther", "Bug", "Flying", 172, 178, 145, 177, 117, 145)
dragonair = Pokemon("Dragonair", "Dragon", None, 134, 149, 128, 168, 134, 134)

jose = Trainer("José", [pikachu, eevee])
robert = Trainer("Robert", [charizard, mewtwo])

separation = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" \
             "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- "
winner = "le vainqueur est "

combattre(jose, robert)
