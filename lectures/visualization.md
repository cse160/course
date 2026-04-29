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

Numeric statistics alone often [fail to represent](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) the [complexity of real datasets](https://en.wikipedia.org/wiki/Datasaurus_dozen). To create visualizations in Python, we need to understand the hierarchy of how code is organized and shared:

- **Package**: A folder that contains multiple modules.
- **Module**: A Python file (e.g., `.py` file) containing related code.
- **Function**: Specific blocks of code inside a module that perform calculations or tasks.

## Matplotlib

**Matplotlib** is a popular Python package with functions used to produce visualizations. It works particularly well when you have two lists of the exact same size:

- **List 1** acts as $x$, the independent variable.
- **List 2** acts as $y$, the dependent variable.

To use Matplotlib functions, we first have to import the `pyplot` module from the `matplotlib` package. We typically give it the alias `plt` to save typing:

```python
import matplotlib.pyplot as plt
```

Here are the most common functions you will use to create and customize line graphs:

- `plt.plot(x_data, y_data)`: Passes in two lists of data. The $x$ values must be provided before the $y$ values. It connects points in the order they appear, so `x_data` should usually be sorted in ascending order. Adding the `label` parameter names the specific line being drawn.
- `plt.xlabel("X Label")`: Passes in a string to label the $x$-axis.
- `plt.ylabel("Y Label")`: Passes in a string to label the $y$-axis.
- `plt.title("Title")`: Passes in a string to title the graph.
- `plt.legend()`: Adds a legend to your graph (requires that you provided a `label` to your plots).
- `plt.savefig("your_filename")`: Passes in a string for the filename. Saves the figure as a `.png` file on your computer.
- `plt.clf()`: Clears the current figure.
- `plt.xlim(low, high)` and `plt.ylim(low, high)`: Limits the visual range of the axes. Both numbers are inclusive.
- `plt.axhline(val)` and `plt.axvline(val)`: Draws a straight horizontal or vertical axis line at the specified value.

> [!warning]
> You must use `plt.clf()` after saving a plot! If you don't reset your plot, you will unintentionally add new data points or lines to the old graph the next time you call `plt.plot()`.

## Practice: StackOverflow Trends

Given the following data representing StackOverflow questions asked over time, write the code to plot both the `avg_questions` and `max_questions` on the same graph. Be sure to include a title, axis labels, and a legend.

```python
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

avg_questions = [60295, 101322, 137951, 170793, 174519, 182860, 181881, 173728, 155569, 146152, 154152, 126301, 109828, 61857, 30926, 8938, 1894]

max_questions = [79909, 115431, 157836, 188754, 207441, 195373, 201905, 201518, 172998, 161134, 186547, 148842, 123576, 87478, 46149, 18897, 1894]

# --- Write your plotting code below ---
import matplotlib.pyplot as plt

plt.plot(years, avg_questions, label="Average")
plt.plot(years, max_questions, label="Max")

plt.title("StackOverflow Years vs. Questions Asked")
plt.xlabel("Years")
plt.ylabel("Questions Asked")
plt.legend()

plt.savefig("stackoverflow_trends")
plt.clf()
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

## Modularization with NFL Data

In a real project, your graphing logic is usually tied together with data processing modules. Imagine building a program to plot average NFL scores across different seasons.

1. **`games.csv`**: The raw data file.
1. **`parse_data.py`**: A Python module that contains a function `load_games(csv_file)` to parse the CSV and return a dictionary representation of the data.
1. **`plot_nfl.py`**: A Python script where you calculate the final list data and generate the graphs.

```python
# Inside plot_nfl.py
import matplotlib.pyplot as plt
from parse_data import load_games

def get_avgs_and_seasons(games):
    # Code to calculate averages from the raw games dictionary
    # ...
    return seasons_list, avg_totals_list

# 1. Load the data using our imported module
games = load_games("games.csv")

# 2. Process the data into plottable lists
seasons, avg_totals = get_avgs_and_seasons(games)

# 3. Plot the data
plt.plot(seasons, avg_totals)
plt.title("Average Total Points per Season")
plt.xlabel("Season")
plt.ylabel("Average Total Points")
plt.savefig("nfl_averages")
plt.clf()
```
