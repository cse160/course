# Name: ...
# CSE 160
# Spring 2026
# Clustering

import os
import math  # noqa: F401
from utils import rounded, parse_args  # noqa: F401


def euclidean_distance(point1, point2):
    """


    >>> rounded(euclidean_distance([0], [1]))
    1.0
    >>> rounded(euclidean_distance([0, 0, 0, 0], [1, 1, 1, 1]))
    2.0
    >>> point1 = [-1, -1, -1, -1]
    >>> point2 = [-5, -3, -1, -1]
    >>> rounded(euclidean_distance(point1, point2))
    4.472

    This function will not modify the given points.

    >>> point1
    [-1, -1, -1, -1]
    >>> point2
    [-5, -3, -1, -1]
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def get_closest_centroid(point, centroids):
    """


    >>> centroids = {"centroid1": [1, 1, 1, 1], "centroid2": [-10.1, 1, 23.2, 5.099]}
    >>> get_closest_centroid([0, 0, 0, 0], centroids)
    'centroid1'
    >>> get_closest_centroid([1.1, 5.3, 55, -12.1], centroids)
    'centroid2'
    >>> get_closest_centroid([0, 0, 0, 0], {
    ...     "centroid1": [10000000000000, 10000000000000, 10000000000000, 10000000000000],
    ...     "centroid2": [1000000000000, 1000000000000, 1000000000000, 1000000000000]}
    ... }))
    'centroid2'

    Centroid names (keys) do not need to follow the "centroid1" and "centroid2" naming scheme.

    >>> get_closest_centroid([10.1, 1], {"c1": [1, 1], "c2": [10, 1], "c3": [-100, 20]})
    'c2'
    >>> get_closest_centroid([0], {"c1": [10], "c2": [0], "c3": [1]})
    'c2'
    >>> get_closest_centroid([0, 0], {"c1": [1, 1], "c2": [1.5, 1.5], "c3": [2, 2]})
    'c1'
    >>> point = [10.1, 1, 23.2, 5.099]
    >>> centroids = {"c1": [1, 1, 1, 1], "c2": [10, 1, 23, 5], "c3": [-100, 20.2, 52.9, -37.088]}
    >>> get_closest_centroid(point, centroids)
    'c2'

    This function will not modify the given points or centroids.

    >>> point
    [10.1, 1, 23.2, 5.099]
    >>> centroids
    {'c1': [1, 1, 1, 1], 'c2': [10, 1, 23, 5], 'c3': [-100, 20.2, 52.9, -37.088]}
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def assign_points_to_centroids(list_of_points, centroids):
    """


    >>> points = [[-1, 1], [1, -1], [1, 1], [-1, -1]]
    >>> centroids = {"c1": [0, 0], "c2": [10, 10]}
    >>> assign_points_to_centroids(points, centroids)
    {'c1': [[-1, 1], [1, -1], [1, 1], [-1, -1]]}
    >>> points = [[0], [1], [2]]
    >>> centroids = {"c1": [10], "c2": [2], "c3": [3]}
    >>> assign_points_to_centroids(points, centroids)
    {'c2': [[0], [1], [2]]}

    This function will not modify the given list of points or centroids.

    >>> points
    [[0], [1], [2]]
    >>> centroids
    {'c1': [10], 'c2': [2], 'c3': [3]}
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def mean_of_points(list_of_points):
    """


    >>> rounded(mean_of_points([[0], [1]]))
    [0.5]
    >>> rounded(mean_of_points([[0, 0, 0, 0], [0, 0, 0, 0]]))
    [0.0, 0.0, 0.0, 0.0]
    >>> rounded(mean_of_points([[1, 2, 4, 6], [3, 4, 6, 8]]))
    [2.0, 3.0, 5.0, 7.0]
    >>> list_of_points = [[-1, -10, -70, -89], [2, 3, 55, 7]]
    >>> rounded(mean_of_points(list_of_points))
    [0.5, -3.5, -7.5, -41.0]

    This function will not modify the given list of points.

    >>> list_of_points
    [[-1, -10, -70, -89], [2, 3, 55, 7]]
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def update_centroids(assignment):
    """


    >>> assignment = {"c1": [[0, 0], [2, 2]], "c2": [[10, 10], [12, 12]]}
    >>> rounded(update_centroids(assignment))
    {'c1': [1.0, 1.0], 'c2': [11.0, 11.0]}
    >>> assignment = {"c1": [[0, 0], [2, 2]]}
    >>> rounded(update_centroids(assignment))
    {'c1': [1.0, 1.0]}

    This function will not modify the given assignment of centroids to lists of points.

    >>> assignment
    {'c1': [[0, 0], [2, 2]]}
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


dataset = parse_args()
if not dataset:
    import doctest
    doctest.testmod()
else:
    from utils import converged, read_data, load_centroids, write_centroids_with_key
    if dataset == "mnist" or dataset == "2d":
        from utils import plot_2d, plot_centroids, plot_fig

    # Load all data, labels, and initial centroids
    data, label = read_data("data/" + dataset + ".csv")
    centroids = load_centroids("data/" + dataset + "_init_centroids.csv")
    if dataset == "mnist":
        plot_centroids(centroids, "init")

    # Run k-means until convergence
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        old_centroids = centroids
        assignment = assign_points_to_centroids(data, old_centroids)
        centroids = update_centroids(assignment)
        step += 1
        if dataset == "2d":
            fig = plot_2d(assignment, centroids)
            results_dir = os.path.join("results", "2D")
            plot_fig(fig, results_dir, "Step " + str(step))
    print("K-means converged after " + str(step) + " steps.")

    if dataset == "mnist":
        plot_centroids(centroids, "final")

    # Save all centroids
    write_centroids_with_key(dataset + "_final_centroids.csv", centroids)


###
# Collaboration and Sources
###

# ... Write your answer here, as comments (lines starting with "#").
