import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(92)
voltaj = np.random.randint(5,20, size=7)
gunler = np.array(["pazartesi", "sali", "carsamba", "persembe", "cuma","cumartesi","pazar"])
df = pd.DataFrame({
    'gunler': gunler,
    'voltaj': voltaj
})
maxVolt= df.loc[df['voltaj'].idxmax(), 'gunler']
minVolt = df.loc[df['voltaj'].idxmin(),'gunler']
print(maxVolt)
print(minVolt)
avVolt = np.mean(df['voltaj'])
print(avVolt)
plt.plot(df['gunler'], df['voltaj'])
plt.axhline(avVolt, color='red', linestyle='--')
plt.legend
plt.show()