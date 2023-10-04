import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

single_sample_size = 100000
coupons = 200

dat = np.zeros(single_sample_size * coupons)
for i in range(coupons):
    df = pd.DataFrame(np.random.geometric((coupons - i) / coupons, size=single_sample_size))
    dat[i * single_sample_size : (i + 1) * single_sample_size] = df.iloc[:, 0]
    #print("collected", i, "unique coupons so far \n", df.head(10))
groupnum = np.arange(1,coupons+1)

df = pd.DataFrame(np.reshape(dat, (coupons, single_sample_size))).transpose()
df.columns = groupnum
df.index = np.arange(1, single_sample_size + 1)
df['sum'] = df.sum(axis=1)
#print(df.head(10))

data = df['sum']
result = sum([1 / x for x in range(1, coupons + 1)]) * coupons
print("Theoretical Mean:",result)

print(data.describe())
range_data = int(data.max()-data.min())
plt.hist(data, bins=coupons, color='gray', edgecolor='black', alpha=0.7)
plt.xlabel('Total Tries')
plt.ylabel('Frequency')
plt.title(f'Tries to get {coupons} Coupons')
plt.xlim(0, data.max())
plt.show()
