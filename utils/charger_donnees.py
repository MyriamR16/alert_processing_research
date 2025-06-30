import pandas as pd

def charger_donnees(chemin_fichier):
    """
    Charge les données depuis un fichier CSV et retourne un DataFrame.
    
    Paramètres :
    chemin_fichier (str) : Chemin vers le fichier CSV.
    
    Retourne :
    pd.DataFrame : Les données chargées sous forme de DataFrame, ou None en cas d'erreur.
    """
    try:
        data = pd.read_csv(chemin_fichier)
        print(f"Chargement réussi du fichier : {chemin_fichier}.")
        return data
    except Exception as e:
        print(f"Erreur lors du chargement des données depuis {chemin_fichier} : {e}")
        return None
