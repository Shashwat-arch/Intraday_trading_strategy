from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, cut_tree, linkage

class FindClustersCenters:
    def __init__(self, extremum:list, algorithm:str, num_clusters:int):
        self.extremum = extremum
        self.algorithm = algorithm
        self.num_clusters = num_clusters

    def fit_algorithm(self):
        extremum = self.extremum
        algorithm = self.algorithm
        num_clusters = self.num_clusters

        if algorithm == 'KMeans':
            kmeans = KMeans(num_clusters)
            kmeans.fit(extremum)
            centroids = kmeans.cluster_centers_
            return centroids.flatten()
        
        elif algorithm == 'Hierarchical':
            pass