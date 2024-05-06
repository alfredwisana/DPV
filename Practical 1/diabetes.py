import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams.update({'font.size': 8, 'font.family': 'sans'})

data = pd.read_csv('diabetes.tab.csv')
print(data.head(20))


# ----------------------------------------
# HISTOGRAM PLOT
# ----------------------------------------

# Mempersiapkan empat tempat kosong untuk diagram 
# Tempat setiap diagram diberi nama ax[0,0]; ax[0,1]; ax[1,0]; ax[1,1]
# Sumbu Y setiap baris akan menggunakan aturan yg sama melalui sharey=True
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, 
                       constrained_layout = True)  # dapat disingkat menjadi plt.subplots(2,2)
fig.set_figheight(6)
fig.set_figwidth(9)


# menampilkan histogram utk BMI dengan lebar bin = 2, jumlah bins akan disesuaikan 
sns.histplot(data, x='BMI', binwidth=2, stat='count', element='bars', palette='coolwarm', ax=ax[0,0])
ax[0,0].set_title('Bin Width = 2')
ax[0,0].set_xlabel('Body Mass Index (kg/m2)')
ax[0,0].set_ylabel('Number of Patients')

# menampilkan histogram utk BMI dengan jumlah bin = 15, lebar bin akan disesuaikan
sns.histplot(data, x='BMI', bins=15, stat='frequency', element='step', ax=ax[0,1])
ax[0,1].set_title('Number of bins = 15')
ax[0,1].set_xlabel('Body Mass Index (kg/m2)')
ax[0,0].set_ylabel('Frequency of the Patients')

# menampilkan histogram utk AGE, garis KDE ditampilkan
sns.histplot(data, x='AGE', stat='density', kde=True, ax=ax[1,0])
ax[1,0].set_title('Age Density')
ax[1,0].set_xlabel('Age of the patients')
ax[1,0].set_ylabel('Density')

# menampilkan histogram utk AGE dengan jumlah bin = 18, lebar bin akan disesuaikan
sns.histplot(data, x='AGE', bins=18, stat='probability', ax=ax[1,1])
ax[1,1].set_title('Age Probability')
ax[1,1].set_xlabel('Age of the Patients')
ax[1,1].set_ylabel('Probability')

plt.suptitle('Histogram - Patients\' BMI Indexes and Age', fontsize=14, fontweight='bold')
plt.show()


# ----------------------------------------
# DENSITY PLOT
# ----------------------------------------

# Dibuat subplot baru dengan sumbu Y dishare (memiliki setting yang sama)
fig, ax = plt.subplots(3, 2, sharey=True, constrained_layout = True)
fig.set_figheight(5.5)
fig.set_figwidth(9)

for i in range(0,3):
    for j in range (0,2):
        bw = round(0.2 + (i*0.4) + (j*0.2), 1)
        if (j%2 != 0): fill=True 
        else: fill=False
        sns.kdeplot(data, x='AGE', bw_adjust=bw, fill=fill, ax=ax[i,j])
        ax[i,j].set_title('Density Plot - Age with bandwidth=' + f'{bw}')
        ax[i,j].set_xlabel('Age')
plt.show()


# ----------------------------------------
# SCATTER PLOT
# ----------------------------------------

sns.set_theme(style="darkgrid")
plt.figure(figsize=(10,6))
sns.scatterplot(data, x='Y', y='BMI',size='AGE', hue='SEX', palette='coolwarm')  # Cari palette lain yang disediakan oleh matplotlib 
plt.title('Progress of Diabetes and BMI Correlations', fontweight='bold')
plt.ylabel('Diabetes Progress')
plt.xlabel('BMI')
plt.show()

