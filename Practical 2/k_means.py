import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA


# Ambil data dari file CSV dan pastikan setiap value bertipe integer 
# ------------------------------------------------------------------
data = pd.read_csv('reviews_u746_a44_2.csv', usecols=['uid','anime_uid','score'] )
data['uid'] = data['uid'].astype(int)
data['anime_uid'] = data['anime_uid'].astype(int)
data['score'] = data['score'].astype(int)
data = data.drop_duplicates(subset=['uid','anime_uid'], keep='first')
# print(data.head(20))
# print(data["uid"].value_counts())


# Struktur data belum sesuai untuk clustering lakukan pivot agar sesuai
# ---------------------------------------------------------------------
pivot = pd.pivot_table(data, values='score', index='uid', columns='anime_uid')
# pivot.fillna(pivot.median(numeric_only=True), inplace = True)
# pivot.fillna(pivot.mean(numeric_only=True), inplace = True)
pivot.fillna(0, inplace = True)
print(pivot.head(10))



# # Mencari jumlah cluster yang paling sesuai untuk data (Elbow method)
# # -------------------------------------------------------------------
# inertias = []
# sscores = []
# for i in range(2,31):
#     model = KMeans(n_clusters=i,n_init=20)
#     model.fit(pivot)
#     labels = model.predict(pivot)
#     inertias.append(model.inertia_)
#     sscores.append(silhouette_score(pivot, labels) * 20000)
    

# plt.plot(range(2,31), inertias, marker='h',markersize=5,linewidth=2,color='blue',linestyle='solid')  # .,ov^<>12348spP*h+xD|_
# plt.plot(range(2,31), sscores, marker='^',markersize=5,linewidth=2,color='red',linestyle='solid')  # .,ov^<>12348spP*h+xD|_
# plt.xticks(range(2, 31))
# plt.title('Elbow & Silhouette Methods')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()




# # Lakukan clustering sesuai jumlah clustering yg disarankan elbow method di atas
# # ------------------------------------------------------------------------------
# n_clusters = 6
# model = KMeans(n_clusters=n_clusters, n_init=20)
# labels = model.fit_predict(pivot)
# # print(model.cluster_centers_)
# print(labels)


# # Buat list yang berisi member tiap cluster
# # -----------------------------------------
# clusters=[]
# for i in range(0,n_clusters): clusters.append([])
# i = 0
# for label in labels:
#     clusters[label].append(pivot.index.values[i])
#     i=i+1


# # Tampilkan barplot yang menunjukkan jumlah member tiap cluster
# # -------------------------------------------------------------
# height = []
# tick_labels = []
# for i in range (0,n_clusters): 
#     height.append(len(clusters[i]))
#     tick_labels.append('C'+str(i))
# plt.bar(range(0,n_clusters), height=height, tick_label=tick_labels,color=['g','y'],edgecolor='r')
# plt.title('Number of Clusters\' members')
# plt.xlabel('clusters')
# plt.yticks(range(0, max(height)+10,10))
# plt.plot(range(0,n_clusters), height, marker='o',markersize=5,linewidth=2,color='red',linestyle='dotted')
# plt.show()


# # Jumlah dimensi terlalu besar (108D) untuk ditampilkan di layar (2D)
# # Kurangi dimensi agar bisa ditampilkan di layar
# # ------------------------------------------------------------------
# dims = PCA(n_components=2,svd_solver='randomized',random_state=0).fit_transform(pivot)
# dims = pd.DataFrame(dims,columns=['PC1','PC2'])
# plt.scatter(dims.loc[:,'PC1'], dims.loc[:,'PC2'],c=labels)
# plt.show()


