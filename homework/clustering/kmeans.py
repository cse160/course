"""
* Name:
* Date:
* CSE 160, Winter 2026
* Homework 4
* Description:
* Collaboration:
"""

from utils import (
    converged, plot_2d, plot_centroids, plot_fig, read_data,
    load_centroids, write_centroids_with_key
    )  # noqa: F401
import math  # noqa: F401
import os


def euclidean_distance(point1, point2):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def get_closest_centroid(point, centroids_dict):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def assign_points_to_centroids(list_of_points, centroids_dict):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def mean_of_points(list_of_points):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def update_centroids(assignment_dict):
    pass  # DELETE THIS LINE AND WRITE YOUR SOLUTION HERE


def main(data, init_centroids, dataset):
    #########################################################################
    # You do not need to change anything in this function.
    # However it is HIGHLY RECOMMENDED to read through and understand what it
    # does. Particularly, the first few lines of the `while` loop show the
    # general flow of the k-means algorithm and how the data flows through
    # the functions you will implement for this assignment.
    #########################################################################
    if dataset == "2d":
        plot_steps, plot_init, plot_final = True, False, False
    elif dataset == "mnist":
        plot_steps, plot_init, plot_final = False, True, True

    centroids = init_centroids
    old_centroids = None
    step = 0

    if plot_init:
        # plot initial centroids
        plot_centroids(centroids, "init")

    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = assign_points_to_centroids(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1

        if plot_steps:
            # plot centroid
            fig = plot_2d(assignment_dict, centroids)
            results_dir = os.path.join("results", "2D")
            plot_fig(fig, results_dir, f"step{step}")

    print(f"K-means converged after {step} steps.")

    if plot_final:
        # plot final centroids
        plot_centroids(centroids, "final")

    return centroids


if __name__ == "__main__":
    dataset = "2d"

    data, label = read_data("data/" + dataset + ".csv")
    init_c = load_centroids("data/" + dataset + "_init_centroids.csv")
    final_c = main(data, init_c, dataset)
    write_centroids_with_key(dataset + "_final_centroids.csv", final_c)
