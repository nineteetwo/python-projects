import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
salesData = np.random.randint(50, 150, size=7)
gunler = np.array(["pazartesi","sali","carsamba","persembe","cuma","cumartesi","pazar"])
birlesim = pd.DataFrame({
    'gun': gunler,
    'satis': salesData
})
maxGun = birlesim.loc[birlesim['satis'].idxmax(), 'gun']
avg_sales = birlesim['satis'].mean()
plt.bar(birlesim['gun'], birlesim['satis'])
plt.title("gun ve satislar")
plt.show()