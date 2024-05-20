import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random,string

# plt.rcParams.update({'font.size': 8, 'font.family': 'sans'})

diabetes = pd.read_csv('diabetes.tab.csv')
# print(diabetes.head())


# # --------------------------------------------------------------
# # Contoh 1-1
# # untuk contoh 1-2, silakan diubah sesuai petunjuk plot
# # --------------------------------------------------------------
# data = (1,2,4,7,9,14)
# data_idx = ('A','B','C','D','E','F')
# data = pd.Series(data, index=data_idx)
# ax = sns.barplot(data, orient='h') 
# for i in ax.containers: ax.bar_label(i)
# plt.show()


# # --------------------------------------------------------------
# # Contoh penggunaan barplot untuk amount dengan tipe lainnya
# # --------------------------------------------------------------
# plt.figure(figsize=(11,6))
# sns.barplot(diabetes, x='AGE', y='BP',estimator='mean',errorbar='sd')
# plt.show()


# # --------------------------------------------------------------
# # Contoh 1-1
# # untuk contoh 1-2, silakan diubah sesuai petunjuk plot
# # --------------------------------------------------------------
# plt.figure(figsize=(11,6))
# sns.countplot(diabetes, x='AGE', stat='count')
# plt.title('1-1. Number of Diabetes Patients by Age')
# plt.yticks(range(0, 20,2))
# plt.show()


# --------------------------------------------------------------
# Contoh 1-3
# --------------------------------------------------------------
# data = (1,2,4,7,9,14)
# data_idx = ('A','B','C','D','E','F')
# data = pd.Series(data, index=data_idx)
# plt.plot(data_idx, data, marker='o', linestyle='none')
# plt.title('1-3. An example of Dot Plot')
# plt.show()


# --------------------------------------------------------------
# Contoh 1-4
# --------------------------------------------------------------
# def random_string(length):
#     return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
# columns = [random_string(5) for i in range(0,15)]
# rows = [random_string(5) for i in range(0,25)]
# data = pd.DataFrame(np.random.randint(0,100,size=(25, 15)), columns=columns, index=rows)
# print(data.head())
# sns.heatmap(data, cmap="magma")
# plt.show()


# --------------------------------------------------------------
# Contoh 1-5
# --------------------------------------------------------------
# sns.countplot(diabetes, x='AGE', hue='SEX')
# plt.title('1-5. Number of Diabetes Patients by Age and Sex')
# plt.show()


# --------------------------------------------------------------
# Contoh 1-5
# --------------------------------------------------------------
# plt.figure(figsize=(10, 6))
# sns.barplot(diabetes.loc[10:50,:], x='AGE', y='BMI', hue='SEX', errorbar=('sd',.5),capsize=.2)
# plt.title('1-5. Number of Diabetes Patients by Age and Sex')
# plt.show()


# --------------------------------------------------------------
# Contoh 1-6
# --------------------------------------------------------------
# x = ['AAA','BBB','CCC','DDD','EEE','FFF']
# data = {'A': [1,2,4,7,9,14], 'B': [3,1,5,3,5,6]}
# bottom = [0,0,0,0,0,0]    # np.zeroes(3)
# for key,val in data.items():
#     plt.bar(x, val, label=key, bottom=bottom)
#     bottom = [bottom[i] + val[i] for i in range(len(bottom))]
# plt.yticks(range(0, 21))
# plt.title("1-6 Stacked Bar")
# plt.legend(loc="upper left")
# plt.show()



# --------------------------------------------------------------
# Contoh 2-1
# --------------------------------------------------------------
# fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, constrained_layout = True)
# fig.set_figheight(6)
# fig.set_figwidth(9)

# sns.histplot(diabetes, x='AGE', hue='SEX', multiple='layer', bins=18, stat='count', ax=ax[0,0])
# ax[0,0].set_xlabel('layer')
# sns.histplot(diabetes, x='AGE', hue='SEX', multiple='dodge', bins=18, stat='count', ax=ax[0,1])
# ax[0,1].set_xlabel('dodge')
# sns.histplot(diabetes, x='AGE', hue='SEX', multiple='stack', bins=18, stat='count', ax=ax[1,0])
# ax[1,0].set_xlabel('stack')
# sns.histplot(diabetes, x='AGE', hue='SEX', multiple='fill', bins=18, stat='count', ax=ax[1,1])
# ax[1,1].set_xlabel('fill')

# plt.suptitle('Histogram', fontsize=14, fontweight='bold')
# plt.show()


# --------------------------------------------------------------
# Contoh 2-2
# --------------------------------------------------------------
# fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, constrained_layout = True)
# sns.kdeplot(diabetes, x='AGE', hue='SEX', multiple='layer', ax=ax[0,0])
# ax[0,0].set_xlabel('layer')
# sns.kdeplot(diabetes, x='AGE', hue='SEX', multiple='stack', ax=ax[0,1])
# ax[0,1].set_xlabel('stack')
# sns.kdeplot(diabetes, x='AGE', hue='SEX', multiple='fill', ax=ax[1,0])
# ax[1,0].set_xlabel('fill')
# ax[1,1].axis('off')

# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
# plt.suptitle('KDE (Density)', fontsize=14, fontweight='bold')
# plt.show()


# --------------------------------------------------------------
# Contoh 2-3
# --------------------------------------------------------------
# sns.ecdfplot(diabetes, x='BP')
# plt.show()


# --------------------------------------------------------------
# Contoh 2-4
# --------------------------------------------------------------
# import statsmodels.api as sm

# # Membuat distribusi normal secara acak dengan mean=50, dan standar deviasi 5
# data = np.random.normal(50, 5, 1000) # (mean, std, size)

# # Bandingkan distribusi di atas dengan distribusi normal yg standar menggunakan QQ plot
# # Skala x dan y berbeda (perhatikan bahwa sumbu y perlu diubah ke 
# # mean dan standar deviasi agar bisa dibandingkan dengan sumbu x)
# sm.qqplot(data, line='45') # line = 45,s,r,q,None
# plt.show()


# --------------------------------------------------------------
# Contoh 2-5
# --------------------------------------------------------------
# sns.catplot(diabetes,x='AGE',y='BMI',kind='box')
# plt.show()
# sns.catplot(diabetes,x='AGE',y='BMI',hue='SEX', kind='box')
# plt.show()


# --------------------------------------------------------------
# Contoh 2-6
# --------------------------------------------------------------
# diabetes = diabetes.loc[(diabetes['AGE'] >= 30) & (diabetes['AGE'] < 50)] 
# sns.catplot(diabetes,x='AGE',y='BMI',kind='violin')
# plt.show()
# sns.catplot(diabetes,x='AGE',y='BMI',hue='SEX', kind='violin')
# plt.show()


# --------------------------------------------------------------
# Contoh 2-7
# --------------------------------------------------------------
# plt.figure(figsize=(10, 6))
# diabetes = diabetes.loc[(diabetes['AGE'] >= 30) & (diabetes['AGE'] < 50)] 
# sns.swarmplot(diabetes, x="AGE", y="BMI",hue='SEX',size=4)
# plt.show()


# --------------------------------------------------------------
# Contoh 2-8
# --------------------------------------------------------------
# diabetes = diabetes.loc[(diabetes['AGE'] >= 30) & (diabetes['AGE'] < 50)] 
# sns.catplot(diabetes,x='AGE',y='BMI',kind='violin')
# sns.swarmplot(diabetes, x="AGE", y="BMI",hue='SEX',size=4)
# plt.show()


# --------------------------------------------------------------
# Contoh 2-11
# --------------------------------------------------------------
# # Membuat contoh data berupa sebuah dataframe dengan 250 baris (integer) dan 2 kolom ()
# isibaris = np.random.randn(250)
# isikolom = np.tile(['A','B','C','D','E'], 50)   # ['A','B','C','D','E','A','B','C','D','E',...]
# df = pd.DataFrame(dict(x=isibaris, y=isikolom))
# print(df.head(20))
# # ... geser data ke kanan sesuai isi kolom y
# df['x'] = np.where(df['y'] =='A', df['x']+1,df['x'])
# df['x'] = np.where(df['y'] =='B', df['x']+2,df['x'])
# df['x'] = np.where(df['y'] =='C', df['x']+3,df['x'])
# df['x'] = np.where(df['y'] =='D', df['x']+4,df['x'])
# df['x'] = np.where(df['y'] =='E', df['x']+5,df['x'])
# # print(df.head(25))

# sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# # siapkan tempat utk beberapa plot sesuai isi kolom 'y'
# fg = sns.FacetGrid(df, row="y", hue="y", aspect=7, height=1)
# # buat density plot pertama dengan fill=true, dan yg kedua dengan garis tepi berwarna putih
# fg.map(sns.kdeplot, "x", bw_adjust=.5, clip_on=False, fill=True, alpha=0.8, linewidth=1.5)
# fg.map(sns.kdeplot, "x", bw_adjust=.5, color='white')
# # kurangi jarak antar plot
# fg.figure.subplots_adjust(hspace=-.4)  

# fg.set_titles("")              # hilangkan judul tiap plot
# fg.set(yticks=[], ylabel="")   # hilangkan tick dan label dari sumbu y di tiap plot
# fg.despine(left=True)          # hilangkan garis untuk skala y
# plt.show()




# --------------------------------------------------------------
# Contoh khusus penggunaan Pair Plot
# --------------------------------------------------------------
# diag = sns.pairplot(diabetes, 
#              x_vars=('AGE','BMI','BP'), 
#              y_vars=('AGE','BMI','BP'), 
#              hue='SEX',  
#              kind='scatter',diag_kind='kde')
# diag._legend.set_bbox_to_anchor((0.6, 0.6))
# plt.show()

# diag = sns.pairplot(diabetes, 
#              x_vars=('AGE','BMI','BP'), 
#              y_vars=('AGE','BMI','BP'), 
#              hue='SEX',  
#              kind='kde',diag_kind='kde')
# diag._legend.set_bbox_to_anchor((0.6, 0.6))
# plt.show()

# diag = sns.pairplot(diabetes, 
#              x_vars=('AGE','BMI','BP'), 
#              y_vars=('AGE','BMI','BP'), 
#              hue='SEX',  
#              kind='hist',diag_kind='kde')
# diag._legend.set_bbox_to_anchor((0.6, 0.6))
# plt.show()


# --------------------------------------------------------------
# Contoh 3-1
# --------------------------------------------------------------
# data = [25,30,35,5,5]
# labels = ['AAA','BBB','CCC','DDD','EEE']

# plt.pie(data, labels=labels, startangle=45, explode = [0, 0, 0, 0.2, 0], autopct='%.2f%%')
# plt.show()


# --------------------------------------------------------------
# Contoh 3-3
# --------------------------------------------------------------
# data1 = [25,30,35,5,5]
# data2 = [10,35,5,5,45]
# data3 = [32,18,27,12,11]
# labels = ['AAA','BBB','CCC','DDD','EEE']

# fig, ax = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=False, constrained_layout = True)

# ax[0].pie(data1, labels=labels, startangle=45, explode = [0, 0, 0, 0.2, 0], autopct='%.2f%%')
# ax[1].pie(data2, labels=labels, startangle=120, explode = [0, 0, 0, 0.2, 0], autopct='%.2f%%')
# ax[2].pie(data3, labels=labels, startangle=0, explode = [0, 0, 0, 0.2, 0], autopct='%.2f%%')
# plt.show()


# --------------------------------------------------------------
# Contoh 3-7
# --------------------------------------------------------------
# from statsmodels.graphics.mosaicplot import mosaic
# data = {('a', 'b'): 1, ('a', 'c'): 2, ('d', 'b'): 3, ('d', 'c'): 4}
# props={}
# props[('a','b')]={'facecolor':'green', 'edgecolor':'white'}
# props[('a','c')]={'facecolor':'red', 'edgecolor':'white'}
# props[('d','b')]={'facecolor':'xkcd:aqua','edgecolor':'white'}
# props[('d','c')]={'facecolor':'xkcd:red','edgecolor':'white'}
# labelizer=lambda k:{('a','b'):1,('a','c'):2,('d','b'):3,('d','c'):4}[k]
# mosaic(data, gap=0, title='a mosaic plot',properties=props, labelizer=labelizer)
# plt.show()


# --------------------------------------------------------------
# Contoh 3-8
# --------------------------------------------------------------
# import plotly.express as px
# datax = { 'kota' : ['Surabaya','Surabaya','Jakarta','Jakarta','Bandung','Bandung'],
#           'penduduk' : ['Penduduk','Penduduk','Bukan','Penduduk','Bukan','Penduduk'], 
#           'JnsKelamin' : ['L','P','P','P','L','L'],
#            'ratagaji' : [1000,2000,3000,4000,5000,6000] } 
# data = pd.DataFrame(data=datax)
# fig = px.treemap(data, path=['kota', 'penduduk'], values='ratagaji')
# fig.show()


# --------------------------------------------------------------
# Contoh 3-9
# --------------------------------------------------------------
# import plotly.express as px

# datax = { 'kota' : ['Surabaya','Surabaya','Jakarta','Jakarta','Bandung','Bandung'],
#           'penduduk' : ['Ya','Ya','Tidak','Ya','Tidak','Tidak'], 
#           'JnsKelamin' : ['L','P','P','P','L','L'] } 
# data = pd.DataFrame(data=datax)
# print(data)

# fig = px.parallel_categories(data, dimensions=['kota','penduduk','JnsKelamin'])
# fig.show()


# --------------------------------------------------------------
# Contoh 4-1 & 4.2
# --------------------------------------------------------------
# sns.set_theme(style="darkgrid")
# plt.figure(figsize=(10,6))
# sns.scatterplot(diabetes, x='Y', y='BMI',size='AGE', hue='SEX', palette='coolwarm') 
# plt.title('Progress of Diabetes and BMI Correlations', fontweight='bold')
# plt.ylabel('Diabetes Progress')
# plt.xlabel('BMI')
# plt.show()


# --------------------------------------------------------------
# Contoh 4-3
# --------------------------------------------------------------
# Data diambil dari https://idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham
# Data di bawah menujukkan volume perdagangan saham untuk 30 perusahaan di hari pertama pasar saham dibuka setelah tahun baru
# datax = {'Comp' : ['AALI','ABBA','ABDA','ABMM','ACES','ACST','ADES','ADHI','ADMF','ADMG','ADMR','ADRO','AGAR','AGII','AGRO','AGRS','AHAP','AIMS','AISA','AKKU','AKPI','AKRA','AKSI','ALDO','ALKA','ALMI','ALTO','AMAG','AMAN','AMAR'],
#          '2022' : [839600,14000300,8463600,27012200,13943000,223200,18570500,70500,1302700,34289600,175091000,15300,15999900,63817300,27237900,3130800,89300,3497600,23100,214900,12962800,106900,12164300,821900,3800,94200,10900,732600,15604100,54700], 
#          '2023' : [337000,1414100,528300,44100900,1370600,68400,5944500,48500,121700,34405500,77679800,5600,5352500,10700500,91243900,1974700,3400,3847800,500,136900,15364300,55300,181300,1419700,48100,407200,16000,99600,10409600,26500] }
# data = pd.DataFrame(datax)

# # Walaupun sebenarnya hanya ada 1 plot (yaitu scatterplot), tetapi tetap secara explisit
# # ditentukan axes (dengan nama variabel ax) agar memudahkan mengatur batas bawah dan atas
# # dari scatterplot tsb. (lihat fungsi set_xlim dan set_ylim di bawah)
# fig, ax = plt.subplots()

# # Menampilkan scatter plot dimana tiap point menunjukkan posisi sebuah perusahaan
# sns.scatterplot(data, x='2022', y='2023',ax=ax)

# # perbedaan nominal jumlah saham yg terlalu besar dari nilai terkecil (puluhan ribu) 
# # ke terbesar (puluhan juta), maka log-scale digunakan agar plot tidak terlalu panjang
# plt.xscale('log') 
# plt.yscale('log')

# # Memastikan sumbu x dan y memiliki batas bawah dan atas yang sama
# min_val = 10000
# max_val = 210000000
# ax.set_xlim(min_val,max_val)
# ax.set_ylim(min_val,max_val)

# # Menampilkan garis diagonal sesuai batas bawah dan atas menggunakan plotline
# plt.plot([min_val,max_val], [min_val,max_val], linestyle = 'dotted')

# # Membuat label untuk tiap point di scatterplot
# for z in range(len(datax['Comp'])):
#     x_pos = datax['2022'][z] * 1.1;
#     y_pos = datax['2023'][z];
#     ax.text(x_pos,y_pos,datax['Comp'][z], alpha=0.6, color='red')

# # Mengatur agar panjang sumbu x dan y secara visual adalah sama
# fig.set_figheight(6)
# fig.set_figwidth(6)

# plt.title('Perbandingan volume saham 30 perusahaan\n di awal tahun 2022 dan 2023', fontweight='bold')
# plt.ylabel('2023')
# plt.xlabel('2022')
# plt.show()


# --------------------------------------------------------------
# Contoh 4-4
# --------------------------------------------------------------
# datax = { 
#     'Pegawai' : ['Andrew','Andrew','Andrew','Bob','Bob','Bob','Charles','Charles','Charles','David','David','David','Edward','Edward','Edward','Frank','Frank','Frank'],
#     'Tahun' : [2018,2020,2022,2018,2020,2022,2018,2020,2022,2018,2020,2022,2018,2020,2022,2018,2020,2022],
#     'Gaji' : [9000000,1050000,14200000,10000000,16000000,18000000,15000000,9000000,13000000,21000000,22000000,23200000,18000000,17000000,15000000,16000000,17300000,19200000],
# }
# data = pd.DataFrame(data=datax)
# print(data)
# sns.pointplot(
#     data=data,
#     x="Tahun", y="Gaji", hue="Pegawai")
# plt.show()


# --------------------------------------------------------------
# Contoh 4-5
# --------------------------------------------------------------
# fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, constrained_layout = True)
# sns.kdeplot(diabetes, x='AGE', y='BMI', ax=ax[0,0])
# ax[0,0].set_xlabel('original plot')
# sns.kdeplot(diabetes, x='AGE', y='BMI', cmap="Reds", shade=True, ax=ax[0,1])
# ax[0,1].set_xlabel('original plot + shade=true + cmap')
# sns.kdeplot(diabetes, x='AGE', y='BMI', cmap="Reds", shade=True, levels=8, ax=ax[1,0])
# ax[1,0].set_xlabel('original plot + shade=true + cmap + level')
# ax[1,1].axis('off')

# fig.set_figheight(6)
# fig.set_figwidth(9)

# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
# plt.suptitle('Density Contours', fontsize=14, fontweight='bold')
# plt.show()


# --------------------------------------------------------------
# Contoh 4-6 & 4-7
# --------------------------------------------------------------
# sns.jointplot(diabetes, x='Y', y='BMI', 
#               kind='hist', 
#               marginal_kws=dict(bins=45), 
#               joint_kws=dict(bins=25),
#               palette='coolwarm') 
# plt.title('Progress of Diabetes and BMI Correlations', y=0.95)
# plt.ylabel('BMI')
# plt.xlabel('Diabetes Progress')
# plt.show()

# sns.jointplot(diabetes, x='Y', y='BMI', 
#               kind='hex', 
#               marginal_kws=dict(bins=35),
#               palette='coolwarm') 
# plt.title('Progress of Diabetes and BMI Correlations', y=0.95)

# plt.ylabel('BMI')
# plt.xlabel('Diabetes Progress')
# plt.xticks(np.arange(0, 350, 25).tolist())
# plt.show()


# --------------------------------------------------------------
# Contoh 4-8
# --------------------------------------------------------------
# sns.heatmap(diabetes.corr(), cmap='magma');
# plt.show()



# --------------------------------------------------------------
# Contoh 4-9
# --------------------------------------------------------------
# saham = pd.read_csv('saham.csv')
# saham = saham.astype({'Tanggal':'datetime64[ns]'})
# print(saham.head())

# sns.lineplot(saham, x='Tanggal', y='UNVR', color='red')
# sns.lineplot(saham, x='Tanggal', y='ASII', color='blue')

# maxDate = saham.Tanggal.max()
# y1 = saham.UNVR.iat[0]  # mencari nilai pada tanggal terakhir di kolom UNVR
# y2 = saham.ASII.iat[0]
# plt.text(np.datetime64(maxDate, 'D'), y1, s='UNVR', color='red')
# plt.text(np.datetime64(maxDate, 'D'), y2, s='ASII', color='blue')

# plt.ylabel("Stock Price (thousands)", fontsize=12)
# plt.xlabel("Date", fontsize=12)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()


# --------------------------------------------------------------
# Contoh 4-10
# --------------------------------------------------------------
# saham = pd.read_csv('saham.csv')
# saham = saham.astype({'Tanggal':'datetime64[ns]'})

# fig, ax = plt.subplots()
# sns.lineplot(saham, x='ASII', y='UNVR', sort=False, ci=None, ax=ax)

# # Membuat label untuk tiap point
# for z in range(len(saham['Tanggal'])):
#     x_pos = saham['ASII'][z];
#     y_pos = saham['UNVR'][z];
#     label = np.datetime64(saham['Tanggal'][z],'D')
#     ax.text(x_pos, y_pos, label, alpha=0.6, color='red')

# plt.show()


# --------------------------------------------------------------
# Contoh 4-11
# --------------------------------------------------------------
# sns.regplot(diabetes,x='BP',y='BMI',order=4)
# plt.show()



# --------------------------------------------------------------
# Contoh 5-1
# --------------------------------------------------------------
# import matplotlib.image as mpimg


# # Refer to https://developers.google.com/machine-learning/crash-course/california-housing-data-description
# housing_df = pd.read_csv('housing.zip')

# # Data preprocessing
# # ... mengisi kolom total_bedrooms menggunakan rata-rata 
# # ... persentase bedroms terhadap total_rooms secara regional
# pct_bedrooms = (housing_df.total_bedrooms / housing_df.total_rooms).agg('nanmean')
# housing_df.total_bedrooms = housing_df.total_bedrooms.fillna(pct_bedrooms * housing_df.total_rooms)
# # ... median income menunjukkan angka seharusnya. Angka yg tersimpan di CSV dalam satuan USD10,000
# housing_df['median_income'] *= 10000
# # ... pastikan beberapa kolom dalam satuan yang tepat sebelum ditampilkan dalam plot
# housing_df = housing_df.astype({'housing_median_age':int, 'total_rooms':int,
#                                 'total_bedrooms':int, 'population':int,
#                                 'households':int })


# # Tampilkan data yang sudah valid ke plot
# img_california = mpimg.imread('california.png')

# plt.figure(figsize=(8.5,6.5))
# ax = plt.scatter(housing_df.longitude, housing_df.latitude,
#             s=housing_df.population/1000,
#             c=housing_df.median_house_value,
#             cmap='jet',
#             alpha=0.25 )
# plt.legend( *ax.legend_elements("sizes",num=5),title='Population x 1000')
# plt.colorbar(pad=0.01).set_label(label='Median House Value', size=12)
# plt.clim(0, 550000)

# plt.imshow(img_california, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.8)
# plt.xlabel("Longitude", fontsize=12)
# plt.ylabel("Latitude", fontsize=12)

# plt.show();