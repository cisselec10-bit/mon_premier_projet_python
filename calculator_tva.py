
#La facture
prix_unitaire = float(input("Prix unitaire HT : "))
quantite = int(input("Quantité : "))
remise = float(input("Pourcentage de remise : "))
tva = float(input("Taux de TVA : "))

# Calcul du total brut HT
total_brut = prix_unitaire * quantite

# Calcul du montant de la remise
montant_remise = total_brut * remise / 100

# Calcul du total HT après remise
total_ht = total_brut - montant_remise

# Calcul du montant de la TVA
montant_tva = total_ht * tva / 100

# Calcul du total TTC
total_ttc = total_ht + montant_tva

# Calcul de l'économie en TTC
economie_ttc = montant_remise * (1 + tva / 100)

# Affichage de la facture
print("\n========== FACTURE ==========")
print(f"Total brut HT : {total_brut:>10.2f} €")
print(f"Remise :       {montant_remise:>10.2f} €")
print(f"Total HT :     {total_ht:>10.2f} €")
print(f"TVA :          {montant_tva:>10.2f} €")
print(f"Total TTC :    {total_ttc:>10.2f} €")
print("-----------------------------")
print(f"Economie TTC : {economie_ttc:>10.2f} €")


