def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" les problèmes sinon

    """

    alerte = False

    if temp <= 18:
        #message = "Température trop basse"
        alerte = True
        # print(message)

    elif temp >= 27:
        alerte = True
        #message = "Température trop élevée"
        #print(message)

    else:
        #message = "Temperature acceptable"
        #print(message)
        alerte = False

    if poussiere == "faible":
        #message = "Poussière acceptable"
        #print(message)
        alerte = False
    elif poussiere == "moyen" or "élevé":
        #message = "Poussière trop élevé"
        #print(message)
        alerte = True

    if 30 <= humidite >= 50:
        #message = "Humidité trop élevé ou trop basse"
        #print(message)
        alerte = True
    else:
        #message = "Humidité bonne"
        #print(message)
        alerte = False

    if not alerte:
        return "Bon environnement"
    else:
        return "Environnement non optimal"



if __name__ == "__main__":
    # TODO: Demander le nom de l'ordi
    # TODO : Créer 3 listes (temp, poussiere, humidités)

    # TODO : Pour le nombre d'ordi
    # TODO : Demander temp, poussiere et humidite
    # TODO : Ajouter les 3 valeurs dans leurs listes respectives

    # TODO : pour nombre d'ordi
    # TODO : vérifier l'environnement : utiliser la fonction et afficher le résultat
    temp = int(input("Entrer la température : "))
    poussiere = input("Entrer l'etat de la poussière [faible, moyen, élevé]: ")
    humidite = float(input("Entrer l'humidité : "))
    environnement_optimal(temp, poussiere, humidite)
