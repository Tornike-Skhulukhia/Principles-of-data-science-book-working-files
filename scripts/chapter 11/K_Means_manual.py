'''
    Use specific data for clustering, save images and generate video
    showing how centroids positions and cluster points change.
    + calculates and shows silhouette_coefficients
'''
import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import shutil
import numpy as np
from pprint import pprint as pp
plt.style.use('dark_background')


df = pd.read_csv('k_means_manual_data_scaled.csv')
COLORS = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan', 'white']

clusters_range = list(range(2, 9))
silhouette_coefficients = []


def draw_centrods(centroids):
    for index, centroid in enumerate(centroids):
        # plt.scatter(*centroid, linewidth=3, marker='+', c=COLORS[index], s=300)
        plt.scatter(*centroid, linewidth=3, marker='+', c='w', s=300)

def draw_clusters(clusters):
    global COLORS

    for cluster_index, cluster_points in clusters.items():
        for point_coords in cluster_points:
            plt.scatter(*point_coords, c=COLORS[cluster_index], alpha=0.5)


def recalculate_centroids(clusters, old_centroids):
    new_centroids = []

    for index, cluster_points in clusters.items():
        if cluster_points:
            x_s = np.array([i[0] for i in cluster_points])
            y_s = np.array([i[1] for i in cluster_points])
            new_centroids.append((x_s.mean(), y_s.mean()))
        else:
            new_centroids.append(old_centroids[index])
    return new_centroids


def generate_animation():
    '''
    get previously saved images and generate video
    '''
    import os
    os.system(f'ffmpeg -r 2 -i k_means_pics/{clusters_num}/%01d.png -vcodec mpeg4 -y -b:v 800k {clusters_num}.mp4')


def calculate_silhouette_coefficient(clusters, centroids):
    all_coefficients = []

    for cluster_index, cluster_points in clusters.items():
        for point_index, (point_x, point_y) in enumerate(cluster_points):
    
            # mean distance to all other points to its cluster
            same_cluster_other_points = [i for index, i in enumerate(cluster_points) if index != point_index]
            a = np.mean([((point_x - x)**2 + (point_y - y)**2)**0.5 for x, y in same_cluster_other_points])
            # mean distance to all other points in the next nearest cluster
            # other_cluster_centroids = centroids[:].pop(cluster_index)
            other_cluster_centroids = [i for index, i in enumerate(centroids) if index != cluster_index]

            for index_, (centroid_x, centroid_y) in enumerate(other_cluster_centroids):
                current_distance = ((point_x - centroid_x)**2 + (point_y - centroid_y)**2)**0.5
                if index_ == 0:
                    nearest_cluster_index = 0
                    nearest_cluster_distance = current_distance
                else:
                    if current_distance < nearest_cluster_distance:
                        nearest_cluster_index = index_
                        nearest_cluster_distance = current_distance
    
            # breakpoint()
            nearest_other_cluster_points = clusters[centroids.index(other_cluster_centroids[nearest_cluster_index])]
            b = np.mean([((point_x - x)**2 + (point_y - y)**2)**0.5 for x, y in nearest_other_cluster_points])
    
            # how it works?
            coefficient = (b-a)/(max(b,a))
            all_coefficients.append(coefficient)
    
    return np.mean(all_coefficients)



# # # to see visually equal length axes
# min_num = int(max(np.floor(df.articles_num.min()), np.floor(df.mean_views_num.min())) - 1)
# max_num = int(max(np.ceil(df.articles_num.max()), np.ceil(df.mean_views_num.max())) + 1)

plt.gca().set_aspect('equal', adjustable='box')
# plt.axis([min_num, max_num, min_num, max_num])

for clusters_num in clusters_range:
    # clusters_num = 3
    print(f'Started clustering with {clusters_num} centroids')
    if os.path.exists(f'k_means_pics/{clusters_num}'): shutil.rmtree(f'k_means_pics/{clusters_num}')
    os.mkdir(f'k_means_pics/{clusters_num}')

    # # cool bug here - if at least one centroid is not lucky at first...
    # centroids = list(zip(
    #                 random.sample(range(min_num, max_num), clusters_num),
    #                 random.sample(range(min_num, max_num), clusters_num)))
    centroids = random.sample(
                            list(zip(df.articles_num, df.mean_views_num)),
                            clusters_num)

    iteration_num = 1
    # save images
    draw_clusters({i:[] for i in range(clusters_num)})
    draw_centrods(centroids)
    plt.savefig(f'k_means_pics/{clusters_num}/{iteration_num}.png')
    plt.clf()

    while True:
        # initilize clusters
        clusters = {i:[] for i in range(clusters_num)}
        centroids_before = centroids.copy()

        # add each point to the nearest cluster
        for _, row in df.iterrows():
            point_x = row.articles_num
            point_y = row.mean_views_num

            # print('Checking point: ', point_x, point_y)
            # get nearest centroid
            for centroid_index, (centroid_x, centroid_y) in enumerate(centroids):
                distance_to_current_centroid = ((point_x - centroid_x)**2 + (point_y - centroid_y)**2)**0.5
                # print('Distance to centroid N', centroid_index, "=", distance_to_current_centroid)

                if centroid_index == 0:
                    # assume first is closest
                    nearest_centroid_index = 0
                    nearest_centroid_distance = distance_to_current_centroid
                else:
                    if distance_to_current_centroid < nearest_centroid_distance:
                            # print('Changed nearest centroid_index')
                            nearest_centroid_index = centroid_index
                            nearest_centroid_distance = distance_to_current_centroid

            # print('Selected centroid index:', nearest_centroid_index)
            # print('='*30)
            clusters[nearest_centroid_index].append((point_x, point_y))
            # print(x, y)


        # recalculate centroids
        centroids = recalculate_centroids(clusters, centroids)
        if centroids_before == centroids: 
            break

        # save images
        draw_clusters(clusters)
        draw_centrods(centroids)
        plt.savefig(f'k_means_pics/{clusters_num}/{iteration_num}.png')
        plt.clf()

        print("Finished iteration N", iteration_num)
        iteration_num += 1


    # df.plot(kind='scatter', x='articles_num', y='mean_views_num')
    # draw_clusters(clusters)
    # draw_centrods(centroids)
    silhouette_coefficients.append(calculate_silhouette_coefficient(clusters, centroids))
    # generate_animation()

plt.plot(clusters_range, silhouette_coefficients)
plt.show()