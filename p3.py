import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("selam")
np.random.seed(42)
sicaklik = np.random.randint(-20,100,size=7)
gunler = np.array(["pazartesi", "sali", "carsamba", "persembe", "cuma","cumartesi","pazar"])
df = pd.DataFrame({
    "gun": gunler,
    'sicaklik': sicaklik
}
)
maxTemp = df.loc[df['sicaklik'].idxmax(), "gun"]
minTemp = df.loc[df['sicaklik'].idxmin(), "gun"]
print(maxTemp)
print(minTemp)
mean =np.mean(sicaklik)
print(mean)
plt.bar(df["gun"], df["sicaklik"])
plt.title("hava durumu")
plt.show()