
#Le chronomètre
secondes = int(input("Entrez le nombre total de secondes : "))

# Conversion en jours
jours = secondes // 86400
reste = secondes % 86400

# Conversion en heures
heures = reste // 3600
reste = reste % 3600

# Conversion en minutes
minutes = reste // 60
reste = reste % 60

# Les secondes restantes
secondes_restantes = reste

# Affichage du résultat
print(f"{jours} j {heures} h {minutes} min {secondes_restantes} s")

# Vérification
verification = (jours * 86400) + (heures * 3600) + (minutes * 60) + secondes_restantes

print(f"Vérification : {verification} secondes")
