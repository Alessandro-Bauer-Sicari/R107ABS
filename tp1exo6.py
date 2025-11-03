minutes_ecoulees = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))
jour = minutes_ecoulees // (24 * 60) + 1  
reste = minutes_ecoulees % (24 * 60)      
heure = reste // 60
minute = reste % 60
print(f"\nNous sommes le jour {jour} à {heure:02d}h{minute:02d}.")
