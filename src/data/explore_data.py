import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configuration des chemins
DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")

def load_data():
    """Charge les données principales."""
    train = pd.read_csv(DATA_DIR / "data_principals/application_train.csv")
    test = pd.read_csv(DATA_DIR / "data_principals/application_test.csv")
    return train, test

def analyze_missing_values(df):
    """Analyse les valeurs manquantes dans le DataFrame."""
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_info = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage': missing_percentage
    })
    return missing_info[missing_info['Missing Values'] > 0].sort_values('Percentage', ascending=False)

def plot_target_distribution(df):
    """Visualise la distribution de la variable cible."""
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='TARGET')
    plt.title('Distribution de la Variable Cible')
    plt.xlabel('TARGET (0: Non-Défaut, 1: Défaut)')
    plt.ylabel('Nombre de Clients')
    plt.savefig(OUTPUT_DIR / 'target_distribution.png')
    plt.close()

def main():
    # Création du dossier outputs s'il n'existe pas
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Chargement des données
    train, test = load_data()
    
    # Analyse des valeurs manquantes
    missing_info = analyze_missing_values(train)
    print("\nAnalyse des valeurs manquantes :")
    print(missing_info)
    
    # Visualisation de la variable cible
    plot_target_distribution(train)
    
    # Statistiques descriptives
    print("\nStatistiques descriptives :")
    print(train.describe())

if __name__ == "__main__":
    main() 