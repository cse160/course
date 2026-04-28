---
kernelspec:
  name: python3
  display_name: Python 3
---

# Clustering

In this homework, we will implement and apply a machine learning algorithm called [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering).

By the end of this assignment, students will feel more comfortable:

1. Writing Python code using lists and dictionaries.
1. Developing Python programs spread over multiple files.
1. Applying a clustering algorithm for data analysis.

## Background

In the real world, quantitative data is rarely ever truly random: they often exhibit patterns that can be extracted with machine learning algorithms. Clustering is one way we can reveal underlying patterns that might be present in the distribution of the data.

Consider the following 2-dimensional dataset. If you were asked to group these points into two clusters, how would you do it? Where would you draw the boundary?

```{code-cell} python
:tags: [remove-input]

import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display
from utils import read_data

data, _ = read_data("data/2d.csv")
data = np.array(data)

fig, ax = plt.subplots(layout="constrained")
ax.scatter(data[:, 0], data[:, 1], c="black", s=15)
ax.set_axis_off()

buf = io.BytesIO()
fig.savefig(buf, format="png")
data_uri = base64.b64encode(buf.getbuffer()).decode("ascii")
display(HTML(f'<img src="data:image/png;base64,{data_uri}" alt="A scatter plot showing several clusters of 2D data points in black.">'))
plt.close(fig)
```

**K-means clustering** works in four steps:

1. Initialize $k$ **centroids** (cluster centers) at random.
1. For each data point in the dataset, assign it to its closest centroid.
1. Update the location of each centroid to the average of all the points assigned to that cluster.
1. Repeat steps 2 and 3 until the centroids no longer change.

As the algorithm iterates, the centroids move towards the center of their assigned points, and the points themselves may be reassigned to a different, closer centroid.

```{code-cell} python
:tags: [remove-input]

import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display
from utils import read_data, load_centroids

# Load all data and initial centroids
data, _ = read_data("data/2d.csv")
centroids = load_centroids("data/2d_init_centroids.csv")

# Convert data and centroids to numpy arrays
data = np.array(data)
centroids = np.array(list(centroids.values()))

# Store the history of (assignments, centroids)
history = []

# Run k-means until convergence
old_centroids = None
while old_centroids is None or not np.allclose(centroids, old_centroids):
    old_centroids = centroids
    distances = cdist(data, centroids, metric="sqeuclidean")
    assignments = np.argmin(distances, axis=1)
    centroids = np.array([
        data[assignments == i].mean(axis=0) if np.any(assignments == i) else centroids[i]
        for i in range(len(centroids))
    ])
    history.append((assignments, centroids))

# Create the animation
fig, ax = plt.subplots(layout="constrained")
colors = ["blue", "red"]
markers = ["o", "^"]

def update(i):
    ax.clear()
    ax.set_axis_off()

    curr_assignments, curr_centroids = history[i]
    for j in range(len(curr_centroids)):
        cluster_points = data[curr_assignments == j]
        # Use different markers for different clusters
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1],
                   c=colors[j], marker=markers[j], s=15)
        # Plot centroids with a bold "X" and white outline to make them pop
        ax.scatter(curr_centroids[j, 0], curr_centroids[j, 1],
                   marker="X", s=800, c=colors[j], edgecolors="white",
                   linewidths=3, label=f"centroid{j}")

    ax.set_title(f"Step {i + 1}")

anim = FuncAnimation(fig, update, frames=len(history), interval=1000)
plt.close()

# Display the animation with a descriptive aria-label
alt_text = "An animation showing the k-means algorithm on 2D data. Two centroids (X markers) start at random positions and move towards the centers of their respective clusters (blue circles and red triangles) over several steps until convergence."
display(HTML(f'<div role="img" aria-label="{alt_text}">{anim.to_jshtml()}</div>'))
```

> [!note]
> **The data points don't change!** Only the centroids change with each iteration. As the centroids move, the data points closest to each centroid can also change.

### Distance metric

How do we know which centroid is closest to each data point? One metric is **Euclidean distance**, which is the straight line distance between two points in a perfect grid. We can calculate the Euclidean distance using the Pythagorean theorem. If we have two points $a = (a_1, a_2, \ldots, a_n)$ and $b = (b_1, b_2, \ldots, b_n)$ in an $n$-dimensional space, the Euclidean distance is the square root of the sum of the squared differences of the points:

$$
D(a, b) = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + (a_n - b_n)^2}
$$ (euclidean-distance)

For example, given two data points from a 3-dimensional dataset `x1 = [-2, -1, -4]` and `x2 = [10, -5, 5]`, the Euclidean distance is: $$\sqrt{(-2  - 10)^2 + (-1 - (-5))^2 + (-4 - 5)^2} = \sqrt{241}$$

### Averaging points

How do we calculate the average of all the points assigned to that cluster? **Take the element-wise average of all data points assigned to that cluster.** If we have three 3-dimensional points $a$, $b$, and $c$, the average is: $$\left[\frac{a_1 + b_1 + c_1}{3}, \frac{a_2 + b_2 + c_2}{3}, \frac{a_3 + b_3 + c_3}{3}\right]$$

For example, given a cluster with three 2-dimensional points:

```python
x1 = [1, 1]
x2 = [2, 3]
x3 = [3, 2]
```

The centroid for this cluster is defined as: $$\left[\frac{1 + 2 + 3}{3}, \frac{1 + 3 + 2}{3}\right] = [2, 2]$$

### Convergence criterion

How do we know our algorithm has converged? **Convergence** occurs when the locations of all centroids only change a miniscule amount between two iterations. We can define a small threshold ($\epsilon$) such that changes smaller than this threshold are ignored.

For example, given two 2-dimensional centroids $c1$ and $c2$:

```python
c1 = [0.45132, -0.99134]
c2 = [-0.34135, -2.3525]
```

After running the next iteration of the algorithm, the centroids are updated to:

```python
c1 = [1.43332, -1.9334]
c2 = [-1.78782, -2.3523]
```

In this case, the algorithm has **not converged** since the location of the two centroids are very different between iterations. However, if the new locations of the centroids are instead:

```python
c1 = [0.45132, -0.99134]
c2 = [-0.34135, -2.3524]
```

Then we can conclude that the algorithm has converged since the locations of the two centroids remained nearly identical (within a certain $\epsilon$) between iterations.

## Part 1: Implementing `kmeans.py`

Let's design and implement the core k-means clustering algorithm by documenting, doctesting, and implementing 5 methods:

1. `euclidean_distance`, which calculates the distance between two points.
1. `get_closest_centroid`, which finds the closest centroid for a point.
1. `assign_points_to_centroids`, which assigns each point to their closest centroid.
1. `mean_of_points`, which calculates the mean of a list of points.
1. `update_centroids`, which updates centroids to the mean of their assigned points.

> [!note]
> This part only requires making changes to the `kmeans.py` file.

The variables `data` and `centroids` follow a particular format.

`data`
: A list of data points, where each data point is a list of floats. For example:

  ```python
  data = [[0.34, -0.2, 1.13, 4.3],
          [5.1, -12.6, -7.0, 1.9],
          [-15.7, 0.06, -7.1, 11.2]]
  ```

  Here, `data` contains three data points. Each data point is four-dimensional. In this example, point 1 is `[0.34, -0.2, 1.13, 4.3]`, point 2 is `[5.1, -12.6, -7.0, 1.9]`, and point 3 is `[-15.7, 0.06, -7.1, 11.2]`.

`centroids`
: A dictionary of centroids, where the keys are string centroid names and the values are lists of centroid locations. For example:

  ```python
  centroids = {
      "centroid1": [1.1, 0.2, -3.1, -0.4],
      "centroid2": [9.3, 6.1, -4.7, 0.18]
  }
  ```

  Here, `centroids` contain two key-value pairs.

  > [!warning]
  > Do not change the names of the centroids when updating their locations.

We have provided several doctests to check your work with the console command:

```ipython
%run kmeans.py
```

### Problem 1: Euclidean distance

Document, doctest, and implement the function `euclidean_distance` that takes two points and returns the Euclidean distance {eq}`euclidean-distance` between them. For example, `euclidean_distance([1.1, 1, 1, 0.5], [4, 3.14, 2, 1])` should return approximately:

```python
3.7735394525564456
```

> [!tip]
> Use the `rounded` function as shown in the given doctests to round the actual results to 3 decimal places (by default).

Likewise, `euclidean_distance([2, 2], [-2, -1])` should return:

```python
5.0
```

### Problem 2: Get the closest centroid

Document, doctest, and implement the function `get_closest_centroid` that takes a point and centroids and returns the centroid closest to the point. For example, `get_closest_centroid([0, 0, 0, 0], {"c1": [1, 1, 1, 1], "c2": [2, 2, 2, 2]})` should return:

```python
'c1'
```

### Problem 3: Assign points to centroids

Document, doctest, and implement the function `assign_points_to_centroids` that takes a list of points and centroids and returns a dictionary assigning each centroid to a list of all points closest to it. For example, given a list of points and centroids dictionary:

```python
list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
centroids = {"centroid1": [1, 1, 1, 1], "centroid2": [2, 2, 2, 2]}
```

Then `assign_points_to_centroids(list_of_points, centroids)` should return:

```python
{'centroid1': [[1.1, 1, 1, 0.5], [0, 0, 0, 0]], 'centroid2': [[4, 3.14, 2, 1]]}
```

If there are no data points assigned to a centroid, exclude that centroid from the result.

### Problem 4: Updating centroids

Document, doctest, and implement the function `mean_of_points` that takes a list of points and returns the average of the points. For example, given list of points:

```python
list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
```

Then `mean_of_points(list_of_points)` should return approximately:

```python
[1.7, 1.38, 1.0, 0.5]
```

Then, document, doctest, and implement the function `update_centroids` that takes an assignment of centroids to their lists of points and returns a new dictionary of centroids representing the cluster average. For example, given an assignment of centroids to their lists of points:

```python
assignment = {
    "centroid1": [[1.1, 1, 1, 0.5], [0, 0, 0, 0]],
    "centroid2": [[4, 3.14, 2, 1]]
}
```

Then `update_centroids(assignment)` should return:

```python
{'centroid1': [0.55, 0.5, 0.5, 0.25], 'centroid2': [4.0, 3.14, 2.0, 1.0]}
```

## Running k-means on 2D data

The code at the bottom of `kmeans.py` loads 2-dimensional data points and initial centroids before running the k-means algorithm and writing the final centroids to a file. You do not need to modify anything in this block of code just yet, but we will make a change in the next part.

Let's run the program from the console with the following command:

```ipython
%run kmeans.py 2d
```

The program should report that it took 7 steps to converge. In addition, there should be 7 plot images generated in a newly-created `results/2D` folder for each of the 7 steps.

## Running k-means on handwriting

After successfully running k-means on 2-dimensional data, let's use it to identify handwritten letters from the **Extended Modified National Institute of Standards and Technology** database (EMNIST). For this assignment, we are only using a small subset of the dataset. Each image is 28-by-28 pixels for a total of 784 pixels per image. For k-means, we treat each image as a 784-dimensional data point.

```{code-cell} python
:tags: [remove-input]
:label: mnist-letter-m

import io
import base64
from IPython.display import HTML, display
from utils import read_data, plot_digit

data, _ = read_data("data/mnist.csv")
fig = plot_digit(data[0])

buf = io.BytesIO()
fig.savefig(buf, format="png")
data_uri = base64.b64encode(buf.getbuffer()).decode("ascii")
display(HTML(f'<img src="data:image/png;base64,{data_uri}" alt="Handwritten letter \'M\'.">'))
plt.close(fig)
```

Let's run the program from the console with the following command:

```ipython
%run kmeans.py mnist
```
The program should report that it took 13 steps to converge.

> [!warning]
> If you see a different number of steps, or it takes longer than a minute or two there may be an error in your code.

In the newly-created `results/MNIST` folder, there should be `init` and `final` folders filled with centroids plotted as images. (You might notice that one of the centroids is missing: you'll investigate it in the next section.)

- The `init` folder contains the initial starting values for the centroids, which look like random noise.
- The `final` folder contains the final values for each centroid after clustering together all similar handwritten letters (data points), which look like actual letters.

How does the algorithm progress from random noise to the final images?

```{code-cell} python
:tags: [remove-input]

import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display
from utils import read_data, load_centroids

# Load all data, labels, and initial centroids
data, labels = read_data("data/mnist.csv")
centroids = load_centroids("data/mnist_init_centroids.csv")

# Convert data, labels, and centroids to numpy arrays
data = np.array(data, dtype=np.uint8)
labels = np.array(labels)
centroids = np.array(list(centroids.values()), dtype=np.float32)

# Store the history of all centroids
history = [centroids]

# Run k-means until convergence
old_centroids = None
while old_centroids is None or not np.allclose(centroids, old_centroids):
    old_centroids = centroids
    distances = cdist(data, centroids, metric="sqeuclidean")
    assignments = np.argmin(distances, axis=1)
    centroids = np.array([
        data[assignments == i].mean(axis=0) if np.any(assignments == i) else centroids[i]
        for i in range(len(centroids))
    ], dtype=np.float32)
    history.append(centroids)

# Identify the centroid that gravitates toward "S"
s_assignments = assignments[np.where(labels == "S")[0]]
s_centroid_idx = np.bincount(s_assignments).argmax()
s_history = [step[s_centroid_idx] for step in history]

# Create the animation
fig, ax = plt.subplots(layout="constrained")
ax.set_axis_off()
img = ax.imshow(s_history[0].reshape(28, 28), cmap="gray")

def update(i):
    img.set_data(s_history[i].reshape(28, 28))
    ax.set_title(f"Step {i}")
    return img, ax.title

# Display the animation
anim = FuncAnimation(fig, update, frames=len(s_history), interval=1000, blit=True)
plt.close()

# Display the animation with a descriptive aria-label
alt_text = "An animation showing a single centroid converging from a random noise pattern into a clear, grayscale handwritten letter 'S' as the k-means algorithm progresses."
display(HTML(f'<div role="img" aria-label="{alt_text}">{anim.to_jshtml()}</div>'))
```

In this animation, centroid {eval}`str(s_centroid_idx)` begins as a random distribution of pixels that gradually converges toward the letter 'S'. Remember that this animation only shows one of the 12 centroids: although several steps appear to make no changes, the 11 other centroids might still be changing.

## Part 2: `analysis.py` and `answers.txt`

In the `"mnist"` dataset, each point represents a single handwritten letter. The goal of the k-means algorithm is to cluster similar data points together in the hope that each of the final centroids ultimately represents a unique letter. In other words, given a new image of a handwritten letter, we can predict the letter by identifying its closest centroid. This is a [machine learning](https://en.wikipedia.org/wiki/Machine_learning) algorithm for handwritten letter recognition!

Machine learning algorithms operate on data, and data in the real world is complicated. Everyone writes a little differently, so handwriting algorithms can hardly ever be truly 100% accurate. To help us evaluate the accuracy of this machine learning algorithm, the `data/mnist.csv` file includes the true label for each data point.

```{literalinclude} data/mnist.csv
:lines: 1
```

This first line for the [handwritten letter "M"](#mnist-letter-m) starts with the character `M` before listing the 784 grayscale pixel values. Let's analyze the results produced by your k-means clustering algorithm.

> [!note]
> This part only requires making changes to the `analysis.py` and `answers.txt` files.

We have provided several doctests to check your work with the console command:

```ipython
%run analysis.py
```

### Problem 5: What happened?

For the `"2d"` dataset, we started with 2 initial centroids and converged to 2 final centroids after 7 steps. But for the `"mnist"` dataset, we started with 12 initial centroids and converged to 11 final centroids after 13 steps. Why are there only 11 centroids left for `"mnist"`? What do you suspect happened? **Write your answers in `answers.txt`.**

> [!tip]
> Start by adding `print` statements to `analysis.py` to investigate the `centroids` dictionary and reviewing the images in `results/MNIST/final`.

### Problem 6: Assigning centroid labels

Document, doctest, and implement the function `assign_labels` that takes a list of points, labels, and centroids and returns a dictionary assigning centroids to lists of the actual labels for each point. For example, given:

```python
list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
labels = ['M', 'W', 'N']
centroids = {"centroid1": [1, 1, 1, 1], "centroid2": [2, 2, 2, 2]}
```

Then `assign_labels(list_of_points, labels, centroids)` should return:

```python
{'centroid1': ['M', 'N'], 'centroid2': ['W']}
```

### Problem 7: Calculate the accuracy

Document, doctest, and implement the function `majority_count` that takes a list of labels and returns the count of the **majority label** (the label that appears most often). For example, `majority_count(['M', 'M', 'N'])` should return `2`.

To evaluate our machine learning algorithm, we can ask: How many of the images labeled as the letter 'K' ended up closest to the same centroid?

Centroid accuracy
: Each centroid predicts its majority label. For example, suppose we have data points with these labels assigned to `centroid1`:

  ```
  Q, Q, Q, Q, Q, Q, O, P, Q, Q, O, P, P, Q, Q
  ```

  Since there are 10 Qs, 3 Ps, and 2 Os in this cluster, we say the label of `centroid1` is Q since it is the label that appears the most frequently. We can then define the accuracy of a centroid's prediction as the majority count divided by the centroid's total number of labels. In this example, the majority label is Q, there are 10 label Q's, and there are 15 total labels for `centroid1`. So the accuracy for `centroid1` is: $$\frac{10}{15} \approx 0.667$$

Overall accuracy
: Overall accuracy is the percentage of correct predictions. Add the majority counts for each centroid and then divide by the total number of labels in the dataset.

Document, doctest, and implement the function `accuracy` that takes a list of points, labels, and centroids and returns the overall accuracy.

### Problem 8: Analyze the Results

In your opinion, looking at the `results/MNIST/final` folder, which letters are easier for the algorithm to distinguish and which are harder? **Write your answer in `answers.txt`.**

> [!tip]
> Alternatively, you can answer this question by instrumenting your `accuracy` function by adding `print` statements to display the accuracy of each centroid. If you add any extra `print` statements for instrumentation or debugging, remove them before submitting your work.

## Code quality

Run our linter (automated code style checker) in the Python console with the expression `!flake8`. Edit the file and save your changes after addressing all reported issues. A successful `!flake8` run will print nothing when there are no linting issues to report.

```ipython
!flake8
```

Then, review our [style guide](../../style-guide.md).

> [!important]
> All functions must include doctests for the given examples.

## Collaboration

If you discuss an assignment with one or more classmates, **you must specify with whom you collaborated in a comment at the bottom of your submission**. You may discuss with as many classmates as you like, but you must cite all of them in your work. Note that you may not collaborate in a way that is prohibited, even if you cite the collaboration.

**At the bottom of your `kmeans.py`, `analysis.py`, and `answers.txt` files**, state which students or other people (besides the course staff) helped you with the assignment, or that no one did.

## Submission

Submit `kmeans.py`, `analysis.py`, and `answers.txt` on Gradescope under the assignment **Homework: Clustering**.
