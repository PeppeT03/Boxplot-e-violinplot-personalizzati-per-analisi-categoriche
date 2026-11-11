# Importazione delle librerie
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Impostiamo il seme per ottenere sempre gli stessi dati casuali
np.random.seed(42)

# Definiamo i giorni della settimana
giorni = ["Lun", "Mar", "Mer", "Gio", "Ven"]

# Definiamo le tre fasce orarie
fasce = ["Mattina", "Pomeriggio", "Sera"]

# CREAZIONE DEL DATASET

data = {
    # Assegniamo casualmente un giorno a ciascuna osservazione
    "giorno": np.random.choice(giorni, 300),

    # Assegniamo casualmente una fascia oraria
    "fascia": np.random.choice(fasce, 300),

    # Generiamo 300 punteggi di soddisfazione:
    # 100 valori con media 7 e deviazione standard 1
    # 100 valori con media 5 e deviazione standard 1.5
    # 100 valori con media 6 e deviazione standard 0.8
    "soddisfazione": np.concatenate([
        np.random.normal(7, 1, 100),
        np.random.normal(5, 1.5, 100),
        np.random.normal(6, 0.8, 100)
    ])
}

# Convertiamo il dizionario in un DataFrame Pandas
df = pd.DataFrame(data)


# PRIMO GRAFICO: BOXPLOT

sns.boxplot(
    data=df,                    # DataFrame utilizzato
    x="giorno",                 # Giorni sull'asse X
    y="soddisfazione",           # Punteggi sull'asse Y
    hue="fascia",               # Distingue le fasce orarie
    palette="Set2",             # Palette di colori
    linewidth=2,                # Spessore delle linee dei box
    order=["Lun", "Mar", "Mer", "Gio", "Ven"],  # Ordine dei giorni
    hue_order=["Mattina", "Pomeriggio", "Sera"]  # Ordine delle fasce
)

# Personalizzazione del grafico
plt.title("Soddisfazione per giorno e fascia oraria")
plt.xlabel("Giorno della settimana")
plt.ylabel("Punteggio di soddisfazione")

# Posizioniamo la legenda all'esterno, sulla destra
plt.legend(
    title="Fascia oraria",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

# Sistemiamo gli spazi e salviamo il grafico
plt.tight_layout()
plt.savefig("esercizio1.png", dpi=300)
plt.show()


# SECONDO GRAFICO: VIOLINPLOT

# Creiamo una nuova figura indipendente
plt.figure(figsize=(10, 6))

sns.violinplot(
    data=df,                    # DataFrame utilizzato
    x="giorno",                 # Giorni sull'asse X
    y="soddisfazione",           # Punteggi sull'asse Y
    hue="fascia",               # Distingue le fasce orarie
    palette="Set2",             # Palette di colori
    split=True,                 # Divide i violini per confrontare i gruppi
    inner="quartile",            # Mostra mediana e quartili all'interno
    order=["Lun", "Mar", "Mer", "Gio", "Ven"],
    hue_order=["Mattina", "Pomeriggio", "Sera"]
)

# Personalizzazione del grafico
plt.title("Distribuzione della soddisfazione per giorno e fascia")
plt.xlabel("Giorno della settimana")
plt.ylabel("Punteggio di soddisfazione")

# Aggiungiamo la legenda all'esterno
plt.legend(
    title="Fascia oraria",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

# Sistemiamo gli spazi e salviamo
plt.tight_layout()
plt.savefig("esercizio1_violin.png", dpi=300)
plt.show()