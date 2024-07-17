import numpy as np
import matplotlib.pyplot as plt
import os

# Daten definieren
x = np.array([ 2, 5, 10, 30, 60, 120, 180])

# Gruppe ATP Cocktail
y1_1 = np.array([	22.69869667,	21.77414667,	20.33294821,	18.42921073,	13.66079392,	8.699737033,	6.008516356])
y1_2 = np.array([	26.50251204,	22.2704322,	    22.23133224,	20.43719907,	16.85805551,	12.74034264,	10.23682161])
y1_3 = np.array([	15.03865558,    14.5870221,	    12.86878852,	10.11979883,	5.492160666,	3.195855269,	2.688679886])


# Gruppe ATP MgATP
y2_1 = np.array([	18.21103728,	17.34906602,	16.05911783,	13.85094548,	9.676707846,	7.061590661,	4.931309762	])
y2_2 = np.array([	13.22681528,	12.3015961,	11.36756779,	9.41986836,	7.308857742,	5.567872061,	4.54418415])
y2_3 = np.array([	15.03865558,	14.5870221,	12.86878852,	10.11979883,	5.492160666,	3.195855269,	2.688679886	])

# Gruppe ATP NADH
y3_1 = np.array([21.99439562,	20.2931843,	20.62072156,	14.03198992,	9.940380282,	5.433450614,	3.187945357,])
y3_2 = np.array([25.08487602,	22.57623158,	22.31992534,	14.78785962,	11.73223929,	7.992628569,	5.544889925,])
y3_3 = np.array([26.60938211,	24.450797,	21.87610768,	15.57428155,	10.95125445,	5.235504159,	4.059436739,])


# Gruppe ATP 2.0
y4_1 = np.array([	14.64984656,	14.53093126,	14.60397639,	14.80389902,	14.66784122,	14.78803214,	14.64094333])
y4_2 = np.array([	21.60126308,	17.69837253,	13.56143121,	13.20550087,	12.64392327,	12.44189901,	12.21941248])
y4_3 = np.array([	15.07796988,	14.93588423,	15.04800841,	14.5501754,	9.493431061,	14.7229126,	16.44473256])


# Gruppe ATP Doppelt
y5_1 = np.array([	15.07507881,	14.92025262,	15.32845738,	14.50746815,	15.1405068,	15.24043936,	15.23232033])
y5_2 = np.array([	16.8225158,	16.79180673,	16.72913388,	16.72626373,	17.08084003,	15.33199149,	16.86398925])
y5_3 = np.array([	16.88792811,	15.4704071,	15.52908056,	15.75985341,	15.96061251,	16.18758986,	19.09118095])




# Mittelwert und Standardabweichung berechnen
y1_mean = np.mean([y1_1, y1_2, y1_3], axis=0)
y1_std = np.std([y1_1, y1_2, y1_3], axis=0)

y2_mean = np.mean([y2_1, y2_2, y2_3], axis=0)
y2_std = np.std([y2_1, y2_2, y2_3], axis=0)

y3_mean = np.mean([y3_1, y3_2, y3_3], axis=0)
y3_std = np.std([y3_1, y3_2, y3_3], axis=0)

y4_mean = np.mean([y4_1, y4_2, y4_3], axis=0)
y4_std = np.std([y4_1, y4_2, y4_3], axis=0)

y5_mean = np.mean([y5_1, y5_2, y5_3], axis=0)
y5_std = np.std([y5_1, y5_2, y5_3], axis=0)

# Plot erstellen
plt.figure(figsize=(10, 8))

# Farben für die Punkte festlegen
color1 = 'red'
color2 = 'green'
color3 = 'blue'
color4 = 'pink'
color5 = 'black'

# Plot für Gruppe ATP Cocktail
plt.errorbar(x, y1_mean, yerr=y1_std, fmt='o', ecolor=color1, alpha=0.2, capsize=5, label='Cocktail', color=color1)
plt.plot(x, y1_mean, linestyle='-', marker='o', color=color1)

# Plot für Gruppe ATP Doppelt
plt.errorbar(x, y2_mean, yerr=y2_std, fmt='o', ecolor=color2,alpha=0.2, capsize=5, label='MgATP', color=color2)
plt.plot(x, y2_mean, linestyle='-', marker='o', color=color2)

# Plot für Gruppe ATP MgATP
plt.errorbar(x, y3_mean, yerr=y3_std, fmt='o', ecolor=color3,alpha=0.2, capsize=5, label='NADH', color=color3)
plt.plot(x, y3_mean, linestyle='-', marker='o', color=color3)

# Plot für Gruppe ATP 2.0
plt.errorbar(x, y4_mean, yerr=y4_std, fmt='o', ecolor=color4,alpha=0.2, capsize=5, label='2.0', color=color4)
plt.plot(x, y4_mean, linestyle='-', marker='o', color=color4)

# Plot für Gruppe ATP NADH
plt.errorbar(x, y5_mean, yerr=y5_std, fmt='o', ecolor=color5,alpha=0.2, capsize=5, label='Doppelt', color=color5)
plt.plot(x, y5_mean, linestyle='-', marker='o', color=color5)





# Plot-Details hinzufügen
plt.xlabel('Minuten')
plt.ylabel('nmol')
plt.title('ATP Vergleich')
plt.legend()
plt.grid(True)

# Pfad zum Speichern definieren
save_path = 'D:/HPLC/Geplottete Daten und Graphen/plot_mit_fehlerindikatoren.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)

# Plot anzeigen
plt.show()