'''
    Use specific data for clustering, save images and generate video
    showing how centroids positions and cluster points change.
'''
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from pprint import pprint as pp
plt.style.use('dark_background')


df = pd.read_csv('k_means_manual_data_scaled.csv')

COLORS = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow']

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


# # # to see visually equal length axes
# min_num = int(max(np.floor(df.articles_num.min()), np.floor(df.mean_views_num.min())) - 1)
# max_num = int(max(np.ceil(df.articles_num.max()), np.ceil(df.mean_views_num.max())) + 1)

plt.gca().set_aspect('equal', adjustable='box')
# plt.axis([min_num, max_num, min_num, max_num])


clusters_num = 3
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
plt.savefig(f'k_means_pics/{iteration_num}.png')
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
    plt.savefig(f'k_means_pics/{iteration_num}.png')
    plt.clf()

    print("Finished iteration N", iteration_num)
    iteration_num += 1


# df.plot(kind='scatter', x='articles_num', y='mean_views_num')
# draw_clusters(clusters)
# draw_centrods(centroids)


def generate_animation():
    '''
    get previously saved images and generate video
    '''
    import os
    os.system('ffmpeg -r 2 -i k_means_pics/%01d.png -vcodec mpeg4 -y -b:v 800k video.mp4')
# generate_animation()


draw_clusters(clusters)
draw_centrods(centroids)
print("Centroids", centroids)
plt.show()

