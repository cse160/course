"""
* Name:
* Date:
* CSE 160, Winter 2026
* Homework 4
* Description:
* Collaboration:
"""

from utils import load_centroids, read_data
from kmeans import get_closest_centroid  # noqa: F401


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS
def assign_labels(list_of_points, labels, centroids_dict):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def majority_count(labels):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def accuracy(list_of_points, labels, centroids_dict):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv", with_key=True)
    # Consider exploring the centroids data here

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))
