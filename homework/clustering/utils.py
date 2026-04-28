# Utility Functions - DO NOT MODIFY THIS FILE!

import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import sys


def rounded(obj, digits=3):
    if isinstance(obj, dict):
        return {k: rounded(v, digits) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [rounded(x, digits) for x in obj]
    elif isinstance(obj, float):
        return round(obj, digits)
    return obj


def read_data(fname):
    data = []
    label = []
    with open(fname, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for r in reader:
            label.append(r[0])
            data.append(list(map(float, r[1:])))
    return data, label


def load_centroids(fname, with_key=False):
    centroids = dict()
    with open(fname, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for i, r in enumerate(reader):
            if with_key:
                centroids[r[0]] = list(map(float, r[1:]))
            else:
                centroids["centroid" + str(i)] = list(map(float, r))
    return centroids


def write_centroids_with_key(fname, centroids):
    with open(fname, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for k, v in centroids.items():
            writer.writerow([k] + v)


def plot_2d(assignment_dict, centroids):
    fig = plt.figure()
    colors = {"centroid0": "blue", "centroid1": "red"}
    for k, v in assignment_dict.items():
        v = np.array(v)
        plt.scatter(v[:, 0], v[:, 1], marker="o", s=15, c=colors[k])
        plt.scatter(centroids[k][0], centroids[k][1], marker="x", s=100, c=colors[k], label=k)
    plt.xlim(-2, 5)
    plt.ylim(-2, 6)
    plt.legend()
    return fig


def plot_digit(digit):
    assert len(digit) == 784
    # mnist digits are size 28 x 28
    im = np.array(digit).reshape(28, 28)
    fig, ax = plt.subplots(layout="constrained")
    ax.set_axis_off()
    plt.imshow(im, cmap="gray")
    return fig


def plot_centroids(centroids, name):
    for k, v in centroids.items():
        fig = plot_digit(v)
        results_dir = os.path.join("results", "MNIST", name)
        plot_fig(fig, results_dir, str(k))


def plot_fig(fig, parent_path, title):
    os.makedirs(parent_path, exist_ok=True)
    plt.title(title)
    fig.savefig(os.path.join(parent_path, title + ".png"))
    plt.clf()
    plt.close()


def converged(c1, c2):
    if c1 is None or c2 is None:
        return False
    for key in c1.keys():
        if not np.allclose(c1[key], c2[key]):
            return False
    return True


def parse_args():
    if len(sys.argv) == 1:
        return None
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        # Print how to use the program correctly if it appears that it has been used incorrectly.
        print("Usage:", sys.argv[0], "<dataset>")
        print("  <dataset> should be either '2d' or 'mnist'")
        print()
        print("  K-means clusters the dataset into a <dataset>_final_centroids.csv file.")
        sys.exit()
