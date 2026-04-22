# Name: ...
# CSE 160
# Spring 2026
# Clustering

import doctest
from utils import rounded, read_data, load_centroids  # noqa: F401
from kmeans import get_closest_centroid  # noqa: F401


def assign_labels(list_of_points, labels, centroids):
    """


    >>> points = [
    ...     [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
    ...     [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
    ...     [ 1.13659605, -2.47109085, -0.83996912, -0.24579457],
    ...     [-1.48090019, -1.47491857, -0.6221167,   1.79055006],
    ...     [-0.31237952,  0.73762417,  0.39042814, -1.1308523 ],
    ...     [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
    ...     [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
    ...     [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
    ...     [-2.01157677,  2.93965872,  0.32334723, -0.1659333 ],
    ...     [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
    ... ]
    >>> labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    >>> centroids1 = {
    ...     "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
    ...     "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
    ...     "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247]
    ... }
    >>> assign_labels(points, labels, centroids1)
    {'centroid3': [0, 1, 2, 1, 2, 2, 0], 'centroid1': [0], 'centroid2': [1, 0]}
    >>> centroids2 = {
    ...     "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
    ...     "centroid2": [10, 10, 10, 10],
    ...     "centroid3": [-10, 1, -10, 10]
    ... }
    >>> assign_labels(points, labels, centroids2)
    {'centroid1': [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]}

    This function will not modify the given list of points, labels, or centroids.

    >>> points
    >>> labels
    [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    >>> rounded(centroids1)  # doctest: +NORMALIZE_WHITESPACE
    {'centroid1': [0.184, -0.458, -1.913, -1.483],
     'centroid2': [-0.718, 1.231, -1.003, -0.382],
     'centroid3': [-1.718, 0.3, 0.003, -0.382]}
    >>> rounded(centroids2)  # doctest: +NORMALIZE_WHITESPACE
    {'centroid1': [0.184, -0.458, -1.913, -1.483],
     'centroid2': [10, 10, 10, 10],
     'centroid3': [-10, 1, -10, 10]}
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def majority_count(labels):
    """


    >>> majority_count([0, 0, 0, 0, 0, 0])
    6
    >>> majority_count([1, 0, 0, 0, 0, 0])
    5
    >>> majority_count([0, 1, 1, 1, 1, 1])
    5
    >>> majority_count([0, 0, 1, 1, 0, 0])
    4
    >>> majority_count([0, 2, 2, 2, 3, 3, 0, 1, 1, 0, 0])
    4
    >>> majority_count([0, 2, 2, 2, 0, 2, 0, 0])
    4
    >>> cats = ["cat", "cat", "cat", "cat", "cat", "cat"]
    >>> majority_count(cats)
    6

    This function will not modify the given labels.

    >>> cats
    ['cat', 'cat', 'cat', 'cat', 'cat', 'cat']
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def accuracy(list_of_points, labels, centroids):
    """


    >>> points = [
    ...     [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
    ...     [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
    ...     [ 1.13659605, -2.47109085, -0.83996912, -0.24579457],
    ...     [-1.48090019, -1.47491857, -0.6221167,   1.79055006],
    ...     [-0.31237952,  0.73762417,  0.39042814, -1.1308523 ],
    ...     [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
    ...     [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
    ...     [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
    ...     [-2.01157677,  2.93965872,  0.32334723, -0.1659333 ],
    ...     [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
    ... ]
    >>> labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    >>> centroids1 = {
    ...     "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
    ...     "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
    ...     "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247]}
    >>> accuracy(points, labels, centroids1)
    0.5
    >>> centroids2 = {
    ...     "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
    ...     "centroid2": [10, 10, 10, 10],
    ...     "centroid3": [-10, 1, -10, 10]}
    >>> accuracy(points, labels, centroids2)
    0.4

    This function will not modify the given list of points, labels, or centroids.

    >>> points
    >>> labels
    [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    >>> rounded(centroids1)  # doctest: +NORMALIZE_WHITESPACE
    {'centroid1': [0.184, -0.458, -1.913, -1.483],
     'centroid2': [-0.718, 1.231, -1.003, -0.382],
     'centroid3': [-1.718, 0.3, 0.003, -0.382]}
    >>> rounded(centroids2)  # doctest: +NORMALIZE_WHITESPACE
    {'centroid1': [0.184, -0.458, -1.913, -1.483],
     'centroid2': [10, 10, 10, 10],
     'centroid3': [-10, 1, -10, 10]}
    """
    pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


data, label = read_data("data/mnist.csv")
centroids = load_centroids("mnist_final_centroids.csv", with_key=True)
# Consider exploring the centroids data here

doctest.testmod()
print(accuracy(data, label, centroids))


###
# Collaboration and Sources
###

# ... Write your answer here, as comments (lines starting with "#").
