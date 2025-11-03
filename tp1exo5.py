jour = int(input("Entrez le numéro du jour (ex : 3) : "))
heure = int(input("Entrez l'heure actuelle (0 à 23) : "))
minute = int(input("Entrez les minutes actuelles (0 à 59) : "))


minutes_ecoulees = ((jour - 1) * 24 * 60) + (heure * 60) + minute


print(f"\nDepuis le début du mois, il s'est écoulé {minutes_ecoulees} minutes.")
