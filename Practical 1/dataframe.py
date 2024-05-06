import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Creating SERIES
# ------------------------------------------------------------

s1 = pd.Series([1, 2.56, "Petra", np.nan, True], name="c1")

s2 = pd.Series([1, 2.56, "Petra", np.nan, True],
               index = ["aa", "bb", "cc", "dd", "ee"])

s3 = pd.Series({"day1": 420, "day2": 380, "day3": 390})

s4 = pd.Series({"day1": 420, "day2": 380, "day3": 390},
               index = ["day1", "day2"])

print('---------- S1 ----------')
print(s1)
print('\n---------- S2 ----------')
print(s2)
print('\n---------- S3 ----------')
print(s3)
print('\n---------- S4 ----------')
print(s4)
print('\n--------------------------')


# ------------------------------------------------------------
# SERIES Functions
# ------------------------------------------------------------

# Hitung jumlah dari non-NaN values
print('Count =', s1.count())

# Hitung jumlah dari NaN values
print('NaN =', s1.isna().sum())

# Cetak frekuensi dari tiap non-NaN value
print('--------------------------')
print(s1.value_counts())

# Konversi series ke list
print('--------------------------')
print(s1.values.tolist())

# Hapus baris dengen index tertentu
s1_fix = s1.drop(index=[2,3])
s1_fix = s1.truncate(before=1, after=3)
print(s1_fix)
print('--------------------------')


# ------------------------------------------------------------
# Creating a DATAFRAME
# ------------------------------------------------------------

data = {
    'c1' : ["qwe","asd","zxc"],
    'c2' : [123,456,789],
    'c3' : [False, True,True],
    'c4' : [4,np.nan,6],
}
df_data = pd.DataFrame(data, index=['a','b','c'])
print(df_data)

print('--------------------------')
print(df_data["c2"])
print('--------------------------')
print(df_data.iloc[0])
print('--------------------------')
df_data.dropna(inplace=True)
print(df_data)

# Mengecek apakah tiap baris memenuhi kondisi ttt.
print('--------------------------')
print(df_data['c2'] > 200)

# Simpan baris-baris di atas ke dataframe baru
print('--------------------------')
df_data2 = df_data[ df_data['c2'] > 200]
print(df_data2)



print('--------------------------')
cars = [["BMW", 3],["Volvo", 7],["Ford", 2]]
df_cars = pd.DataFrame(cars,
                 index=["a",200,4.56],
                 columns=["abc","def"])
print(df_cars)

