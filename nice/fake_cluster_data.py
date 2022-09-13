import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import seaborn as sns
sns.set()
# First I want to remember how to apply kmeans
 #Make features and targets with 1000 samples,
features, target = make_blobs(n_samples=1000, n_features=2,centers=10,
                              cluster_std=0.60, shuffle=True)
#Now we visualize our data
colors = sns.color_palette("hls", 10)
plt.scatter(features[:,0], features[:,1], label="Features")
plt.legend()
plt.show()