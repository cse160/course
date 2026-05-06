---
exports:
  - format: typst
    template: ./
    id: visualization-handout
downloads:
  - id: visualization-handout
    title: Handout
---

# Visualization

Quantitative research can be understood in terms of inputs and outputs:

- The **input**, $x$, is the independent variable that the researcher controls.
- The **output**, $y$, is the dependent variable resulting from running an experiment given the input $x$.

For example, suppose we ran an experiment that produced the following two lists representing `x` and `y`, respectively. How would you explain the relationship between `x` and `y`? We could try computing the mean (average) using `for` loops or by using built-in functions like `sum` and `len`.

```python
[4,    5,    6,    7,    8,    9,    10,   11,   12,    13,   14  ]
[4.26, 5.68, 7.24, 4.82, 6.95, 8.81, 8.04, 8.33, 10.84, 7.58, 9.96]
```

What about this experiment that produced different `y` values given the same `x` values?

```python
[4,    5,    6,    7,    8,    9,    10,   11,    12,   13,   14  ]
[3.10, 4.74, 6.13, 7.26, 8.14, 8.77, 9.14, 9.26,  9.13, 8.74, 8.10]
```

[Descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics) like the mean, median, and standard deviation often fail to represent the complexity of datasets! [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) demonstrates the importance of visualization as a means of understanding data.

## Matplotlib

**Matplotlib** is a popular Python package with functions used to produce visualizations.

Package
: A folder that contains multiple modules.

Module
: A `.py` file containing related code.

To use Matplotlib functions, we first have to import the `pyplot` module from the `matplotlib` package. We typically give it the alias `plt`:

```python
import matplotlib.pyplot as plt
```

Here are the most common functions you will use to create and customize line graphs:

- `plt.plot(x_data, y_data, label="Your Label")`: Plots points in the order they appear, so `x_data` should usually be sorted in ascending order. Specifying the `label` parameter names the specific line being drawn.
- `plt.xlabel("X Label")`: Labels the $x$-axis.
- `plt.ylabel("Y Label")`: Labels the $y$-axis.
- `plt.title("Title")`: Titles the graph.
- `plt.legend()`: Adds a legend to your graph (assuming you provided a `label` for your data).
- `plt.savefig("your_filename")`: Saves the figure as a `.png` file on your computer.
- `plt.clf()`: Clears the current figure.
- `plt.xlim(low, high)` and `plt.ylim(low, high)`: Limits the visual range of the axes. Both numbers are inclusive (unlike the `range` function).
- `plt.axhline(val)` and `plt.axvline(val)`: Draws a straight horizontal or vertical axis line at the specified value.

> [!warning]
> You must use `plt.clf()` after saving a plot! If you don't reset your plot, you will unintentionally add new data points or lines to the old graph the next time you call `plt.plot()`.

## Practice: Stack Overflow Trends

Stack Overflow is an online Q&A discussion forum for computer programming. Given the average questions asked per month and the maximum questions asked per month for each year from 2010 through January 2026, write code to plot both the `avg_q` and `max_q` on the same figure. Be sure to include a title, axis labels, and a legend.

```python
years = [ 2010,   2011,   2012,   2013,   2014,   2015,   2016,
          2017,   2018,   2019,   2020,   2021,   2022,   2023,
          2024,   2025,   2026]
avg_q = [60295, 101322, 137951, 170793, 174519, 182860, 181881,
        173728, 155569, 146152, 154152, 126301, 109828,  61857,
         30926,   8938,   1894]
max_q = [79909, 115431, 157836, 188754, 207441, 195373, 201905,
        201518, 172998, 161134, 186547, 148842, 123576,  87478,
         46149,  18897,   1894]
```

## Practice: x versus y

What will happen when we run this program?

```python
x_vals = [1, 2, 3, 4]
y_vals = [10, 20, 30]

plt.plot(x_vals, y_vals)
plt.savefig("plot_1")
```

## Practice: Will it plot?

What is different between these two programs' outputs?

```python
x_vals = [1, 2, 3, 4]
y1_vals = [10, 20, 30, 70]
y2_vals = [20, 50, 40, 90]

plt.plot(x_vals, y1_vals)
plt.plot(x_vals, y2_vals)
plt.savefig("image")
plt.clf()
```

```python
x_vals = [1, 2, 3, 4]
y1_vals = [10, 20, 30, 70]
y2_vals = [20, 50, 40, 90]

plt.plot(x_vals, y1_vals)
plt.savefig("image_1")
plt.clf()

plt.plot(x_vals, y2_vals)
plt.savefig("image_2")
plt.clf()
```

## Example: NFL scores

Given `games.csv`, a CSV file containing average NFL scores across different seasons, decompose the problem into one or more functions that ultimately plot the average total points per season. What functions would we need to write so that the following code works?

```python
plt.plot(seasons, avg_totals)
plt.title("Average Total Points per Season")
plt.xlabel("Season")
plt.ylabel("Average Total Points")
plt.savefig("nfl_averages")
plt.clf()
```
