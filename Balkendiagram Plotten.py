import matplotlib.pyplot as plt
import numpy as np
import os

# Beispiel-Daten, die dem hochgeladenen Diagramm ähneln
labels = ['12mM MgSO4', '20mM MgSO4', '12mM MgCl2']
values = [0.128292806, 0.122056471, 0.143413741]
colors = ['blue', 'orange', 'green']

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
bars = plt.bar(np.arange(len(labels)), values, color=colors)

# Achsenbeschriftungen und Titel
plt.ylabel('nmol/min/µg')
plt.title('Magnesium Comparison')
plt.xticks(np.arange(len(labels)), labels)


# Pfad zum Speichern definieren
save_path = 'D:\Platereader/Balkendiagramm.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)


# Plot anzeigen
plt.show()