import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Importe tes utilitaires (adapter le chemin si besoin)
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from charger_donnees import charger_donnees
from compter_alertes import compter_alertes_par_ip

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data_raw', 'logs')

def list_log_files(data_dir):
    log_files = []
    for root, _, files in os.walk(data_dir):
        for f in files:
            if f.endswith(".csv") or f.endswith(".log"):
                log_files.append(os.path.join(root, f))
    return log_files

def compter_types_attaques(data, attack_col='Label'):
    if attack_col in data.columns:
        return data[attack_col].value_counts()
    else:
        print(f"⚠️ Colonne '{attack_col}' non trouvée dans les données.")
        return pd.Series()

def main():
    log_files = list_log_files(DATA_DIR)
    print(f"Fichiers trouvés : {len(log_files)}")
    if len(log_files) == 0:
        print("Aucun fichier de logs trouvé. Vérifie le chemin DATA_DIR.")
        return

    # Charge le premier fichier pour test
    data = charger_donnees(log_files[0])
    if data is None:
        print("Erreur chargement fichier.")
        return

    print(f"Données chargées : {data.shape[0]} lignes, {data.shape[1]} colonnes")

    # Nb total alertes
    print(f"Nombre total d’alertes : {len(data)}")

    # Nb alertes par IP
    nb_alertes_ip = compter_alertes_par_ip(data, ip_col='Source IP')
    print("\nNombre d’alertes par IP :")
    print(nb_alertes_ip.head(10))

    # Distribution des types d'attaques
    repartition_attaques = compter_types_attaques(data, attack_col='Label')
    print("\nRépartition des types d’attaques :")
    print(repartition_attaques)

    # Affiche un graphe barres pour la répartition des attaques
    repartition_attaques.plot(kind='bar', title='Répartition des types d\'attaques')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
