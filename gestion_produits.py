class GestionProduits:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.produits = self.charger_produits()

    def charger_produits(self):
        produits = []
        with open(self.nom_fichier, "r") as f:
            for ligne in f:
                nom, prix, quantite = ligne.strip().split(',')
                produits.append({'nom': nom, 'prix': float(prix), 'quantite': int(quantite)})
        return produits

    def enregistrer_produits(self):
        with open(self.nom_fichier, "w") as f:
            for produit in self.produits:
                f.write(f"{produit['nom']},{produit['prix']},{produit['quantite']}\n")

    def ajouter_produit(self):
        nom = input("Nom du produit : ")
        prix = float(input("Prix du produit : "))
        quantite = int(input("Quantité du produit : "))
        self.produits.append({'nom': nom, 'prix': prix, 'quantite': quantite})
        print(f"Produit '{nom}' ajouté.")

    def supprimer_produit(self):
        nom = input("Nom du produit à supprimer : ")
        self.produits = [p for p in self.produits if p['nom'] != nom]
        print(f"Produit '{nom}' supprimé.")

    def rechercher_produit(self):
        nom = input("Nom du produit à rechercher : ")
        for produit in self.produits:
            if produit['nom'] == nom:
                print(f"{produit['nom']} - Prix: {produit['prix']}€ - Quantité: {produit['quantite']}")
                return
        print("Produit non trouvé.")

    def recherche_binaire(self):
        nom = input("Nom du produit à rechercher : ")
        produits_tries = sorted(self.produits, key=lambda p: p['nom'])  
        bas = 0
        haut = len(produits_tries) - 1
        while bas <= haut:
            milieu = (bas + haut) // 2
            if produits_tries[milieu]['nom'] == nom:
                return produits_tries[milieu]
            elif produits_tries[milieu]['nom'] < nom:
                bas = milieu + 1
            else:
                haut = milieu - 1
        print(milieu)
        return None

    def tri_bulles(self, critere='prix'):
        n = len(self.produits)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.produits[j][critere] > self.produits[j + 1][critere]:
                    self.produits[j], self.produits[j + 1] = self.produits[j + 1], self.produits[j]

    def tri_rapide(self, critere='prix'):
        """if len(self.produits) <= 1:
            return self.produits
        pivot = self.produits[len(self.produits) // 2][critere]
        gauche = [p for p in self.produits if p[critere] < pivot]
        centre = [p for p in self.produits if p[critere] == pivot]
        droite = [p for p in self.produits if p[critere] > pivot]
        return self.tri_rapide(gauche) + centre + self.tri_rapide(droite)"""
        print('indisponible')

    def afficher_produits(self):
        if not self.produits: 
            print("Aucun produit disponible.")
        else:
            for produit in self.produits:
                print(f"{produit['nom']} - Prix: {produit['prix']}€ - Quantité: {produit['quantite']}")
