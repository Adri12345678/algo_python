from gestion_produits import GestionProduits

def menu():
    nom_fichier = "produits.txt"
    gestion = GestionProduits(nom_fichier)
    
    while True:
        print("\nMenu:")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Rechercher un produit")
        print("4. Trier les produits")
        print("5. Afficher les produits")
        print("6. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            gestion.ajouter_produit()
            gestion.enregistrer_produits()

        elif choix == "2":
            gestion.supprimer_produit()
            gestion.enregistrer_produits()

        elif choix == "3":
            print('1. Recherche noramle')
            print('2. Recherche binaire')
            choix = input("Entrer une option :")
            if choix == '1':
                gestion.rechercher_produit()
            elif choix == '2':
                gestion.recherche_binaire()
            else:
                print("erreur dans le choix")

        elif choix == "4":
            critere = input("Trier par (prix/quantite) : ")
            if critere not in ['prix', 'quantite']:
                print("Critère invalide.")
            else:
                algorithme = input("Choisissez un algorithme de tri (bulles/rapide) : ")
                if algorithme == 'bulles':
                    gestion.tri_bulles(critere)
                elif algorithme == 'rapide':
                    gestion.tri_rapide(critere)
                else:
                    print("Algorithme invalide.")

        elif choix == "5":
            gestion.afficher_produits()

        elif choix == "6":
            gestion.enregistrer_produits()
            print("Au revoir !")
            break
        
        else:
            print("Option invalide. Essayez à nouveau.")

if __name__ == "__main__":
    menu()
