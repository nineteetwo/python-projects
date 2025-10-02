import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(92)
gunler = np.array(["pazartesi", "sali", "carsamba", "persembe", "cuma", "cumartesi", "pazar"])
derece = np.random.randint(-50, 50, size=7)
nem = np.random.randint(30, 80, size=7)
ruzgarHizi = np.random.randint(5, 20, size=7)
voltaj = np.random.randint(5, 20, size=7)

df = pd.DataFrame({
    'gunler': gunler,
    'derece': derece,
    'nem': nem,
    'ruzgar hizi': ruzgarHizi,
    'elektrik tuketimi': voltaj
})
maxDerece = df.loc[df['derece'].idxmax(), 'gunler']
minDerece = df.loc[df['derece'].idxmin(), 'gunler']
maxNem = df.loc[df['nem'].idxmax(), 'gunler']
minNem = df.loc[df['nem'].idxmin(), 'gunler']
maxRuzgar = df.loc[df['ruzgar hizi'].idxmax(), 'gunler']
minRuzgar = df.loc[df['ruzgar hizi'].idxmin(), 'gunler']
maxVoltaj = df.loc[df['elektrik tuketimi'].idxmax(), 'gunler']
minVoltaj = df.loc[df['elektrik tuketimi'].idxmin(), 'gunler']
avDerece = np.mean(df['derece'])
avNem = np.mean(df['nem'])
avRuzgar = np.mean(df['ruzgar hizi'])
avVoltaj = np.mean(df['elektrik tuketimi'])
fig, axs = plt.subplots(1,3)
axs[0].scatter(df['derece'], df['elektrik tuketimi'])
axs[2].boxplot(df['elektrik tuketimi'])
axs[1].plot(df['gunler'], df['elektrik tuketimi'], color='yellow',label='elektrik tuketimi')
axs[1].plot(df['gunler'], df['nem'], color='blue',label='nem')
axs[1].plot(df['gunler'], df['derece'], color='red', label = "hava derecesi")
axs[1].plot(df['gunler'], df['ruzgar hizi'], color='black', label="ruzgar hizi")
plt.tight_layout()
axs[1].legend(loc='upper right')
plt.show()
#korelasyon ogren ve bu koda uygula.