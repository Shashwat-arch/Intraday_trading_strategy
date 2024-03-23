import numpy as np
import matplotlib.pyplot as plt

class MakePlot:
    def __init__(self, avg_values:list, centroids:list):
        self.avg_values = avg_values
        self.centroids = centroids

    def scatter_plot(self):
        indices1 = np.arange(len(self.avg_values))
        indices2 = np.arange(len(self.centroids))
        plt.figure(figsize=(20, 10))
        plt.plot(indices1, self.avg_values, marker='v', linestyle='-', color='g', label='Data')

        #plt.plot(indices2, centroid_values, marker='o', linestyle='', color='r', markersize=10, label='Centroids')
        for i, centroid in enumerate(self.centroids):
            plt.hlines(centroid, xmin=0, xmax=len(self.avg_values)-1, colors='r', linestyles='dashed')

        plt.grid(True)
        plt.legend()

        plot_filename = 'static/plot.png'
        plt.savefig(plot_filename)

        plt.close()

        return plot_filename