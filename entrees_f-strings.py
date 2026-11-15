

#Manipuler les entrées et les f-strings

#Saisie prénom
prenom = input("Saisissez votre prénom : ")

#Saisie nom
nom = input("Saisissez votre non :")

#Saisie année de naissance
an_naiss = int(input("Saisissez votre année de naissance :"))

#Saisie année en cours
an_actu = int(input("Saisissez l'année actuelle :"))

#Calculer âge en année
age = an_actu - an_naiss 

#Calculer âge en jours
age_jours = age * 365

#Calculer âge en heures
age_heure = age_jours * 24

#Calculer âge en minutes
age_minutes = age_heure * 60

# Affichage de la fiche
print("--------- FICHE D'IDENTITE ---------")
print(f"Prénom : {prenom}")
print(f"Nom : {nom.upper()}")
print(f"Âge : {age} ans")
print(f"Jours vécus = {age_jours}")
print(f"Heures vécues = {age_heure}")
print(f"Minutes vécues = {age_minutes}")

# Affichage des initiales
initiales = prenom[0].upper() + nom[0].upper()
print(f"Initiales : {initiales}")

