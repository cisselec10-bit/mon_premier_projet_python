

#Manipuler les entrées et les f-strings

#Saisie prénom
prenom = input("Saisissez votre prénom : ")
print(f"Votre prénom est : {prenom}")

#Saisie nom
nom = input("Saisissez votre non :")
print(f"Votre nom est : {nom}")

#Saisie année de naissance
an_naiss = int(input("Saisissez votre année de naissance"))
print(f"Vous êtes né(é) en :{an_naiss}")

#Saisie année en cours
an_actu = int(input("Saisissez l'année actuelle"))
print(f"Année actuelle est :{an_actu}")

#Calculer âge en année
age = an_actu - an_naiss 
print(f"Vous êtes agé(e) de :{age} ans")

#Calculer âge en jours
age_jours = age * 365
print(f"Vous êtes agé(e) de :{age_jours} jours")

#Calculer âge en heures
age_heure = age_jours * 24
print(f"Vous êtes agé(e) de :{age_heure} heures")

#Calculer âge en minutes
age_minutes = age_heure * 60
print(f"Vous êtes agé(e) de :{age_minutes} minutes")
