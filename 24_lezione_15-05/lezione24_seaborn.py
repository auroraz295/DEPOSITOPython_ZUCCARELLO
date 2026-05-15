import matplotlib.pyplot as plt
import seaborn as sns 

#GRAFICO A BARRE
sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Conto totale per giorno")

plt.show()

#GRAFICO A LINEE
fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.title("Segnale FMRI nel tempo")

plt.show()

#ISTOGRAMMA E KDE
data = sns.load_dataset("penguins")

sns.histplot(data=data, x="flipper_length_mm", kde=True)
plt.title("Distribuzione lunghezza pinne dei pinguini")

plt.show()

#SE SI VOGLIONO FAR APPARIRE PIU' GRAFICI BISOGNA USARE PLT.FIGURE(), ALTRIMENTI NON C'E' BISOGNO 