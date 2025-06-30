import pandas as pd

def compter_alertes_par_ip(data, colonne_ip):
    """
    Compte le nombre d'alertes pour chaque adresse IP unique dans la colonne spécifiée.
    
    Paramètres :
    data (pd.DataFrame) : DataFrame contenant les alertes.
    colonne_ip (str) : Nom de la colonne contenant les adresses IP.
    
    Retourne :
    Série (pd.Series) avec les adresses IP en index et le nombre d'occurrences en valeur.
    """
    return data[colonne_ip].value_counts()
