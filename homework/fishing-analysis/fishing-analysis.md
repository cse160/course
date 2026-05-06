---
kernelspec:
  name: python3
  display_name: Python 3
---

# Fishing Analysis

In this homework, we will define our own classes to parse and analyze worldwide fish consumption, farming, and catching data as they relate to national population metrics over time.

By the end of this assignment, students will feel more comfortable:

1. Writing classes that enable statistical data analysis.
1. Processing large datasets in comma-separated values (CSV) file format.
1. Creating data visualizations with matplotlib.

## Background

Fish is a major source of protein and nutrition around the world. Increasing worldwide population has led to increasing fish consumption, fish farming, and fish catching. But is demand outstripping supply? Is the world experiencing overfishing? And, if current trends continue, will we run out fish in the future? Organizations such as the [United Nations Food and Agriculture Organization](https://en.wikipedia.org/wiki/Food_and_Agriculture_Organization) track this data to assess the impacts of supply and demand on food systems and sustainability.[^1]

[^1]: Hannah Ritchie and Max Roser. 2021. "Fish and Overfishing." In _OurWorldinData.org_. <https://ourworldindata.org/fish-and-overfishing>

We've prepared two datasets, `small.csv` and `large.csv`, that both share the same columns:

1. `country`, such as _United States_
1. `country code`, such as _USA_
1. `measure`, which will be either _wild caught_, _farmed_, _consumption_, or _population_
1. and columns for each year, such as `1995`, `1996`, `1997`.

Each year column represents the value of the `measure` in that year. There will be the proper number of commas to represent every year mentioned on the header row, but not all years are guaranteed to have values. Can you spot the missing value in the `small.csv` file?

```{literalinclude} small.csv
```

The first row for the `country` _United States_ is missing a data point for the `measure` _consumption_ in the year `1998`!

```csv
United States,USA,consumption,21.96,21,20.96,,21.6,22.04
```

## Problem 0: Dataset comprehension

Answer the following questions in `answers.txt`. You may find it helpful to read the entire assignment instructions.

1. Why are there multiple rows for each country? Why isn't there just a single row for each country?
1. What do you notice about the data for 1998? How will this affect how you'll handle reading the data in this problem's functions?
1. The measure _consumption_ is clearly labeled in the dataset, but no lines directly measure the _production_. How do you determine how much fish was produced by Canada in 1995? (Hint: the answer to this specific question is 1013617.)

## Problem 1: `Country` class

### Problem 1a: Initialization

Document and implement the `__init__` method that takes `self`, the `name` of a country, the `start_year`, and the `end_year` and initializes the following fields:

- `self.name`: The name of the country given as an argument.
- **Empty dictionaries** for each `measure` that will be given by the `update_data` method:
  - `self.farmed`
  - `self.wild_caught`
  - `self.consumption`
  - `self.population`
- **Empty dictionaries** for two more measures we will calculate:
  - `self.production`
  - `self.need`

Notice that `self.years` has already been initialized for you to be a list of integers between `start_year` and `end_year` (inclusive).

We have provided several doctests to check your work with the console command:

```ipython
%run fishing.py
```

### Problem 1b: Update data

Document and implement the `update_data` method that takes `self` and a `row` and updates `self` to match the given `row`. Years are converted to `int` values, measurements are converted to `float` values, and missing measurements are represented with `None`.

`row`
: A **dictionary** representation of one row of data as provided by `csv.DictReader`.

  The row `United States,USA,consumption,21.96,21,20.96,,21.6,22.04` would be represented in Python as:

  ```python
  row = {
      "country": "United States",
      "country code": "USA",
      "measure": "consumption",
      "1995": "21.96",
      "1996": "21",
      "1997": "20.96",
      "1998": "",
      "1999": "21.6",
      "2000": "22.04"
  }
  ```

  > [!warning]
  > `csv.DictReader` reads all content as strings, such as `'1995'` and `'22.62'`.

Running `update_data` on this `row` would result in the following dictionary updates:

```python
self.consumption[1995] = 21.96
self.consumption[1996] = 21.0
self.consumption[1997] = 20.96
self.consumption[1998] = None
self.consumption[1999] = 21.6
self.consumption[2000] = 22.04
```

Remember to use `self.years` to iterate through the years!

### Problem 1c: Actual production

Document and implement the `calc_actual_production` method that takes `self` and a `year` and updates the `self.production` dictionary with an entry for the country's **actual production** in the given year.

actual production
: The sum of the _farmed_ and _wild caught_ values for the country in the given year.

For example, in `small.csv`, the production of Canada in 1995 was 1013617: the sum of the _farmed_ amount 65207 and the _wild caught_ amount 948410. `self.production` should have an updated entry for the year 1995:

```python
{1995: 1013617.0}
```

While you may assume `self.farmed` and `self.wild_caught` will not be empty, note that they may still contain missing measurements for a given `year`. To handle these missing values:

- If **both** farmed and wild caught data are missing for the given `year` for this country, then the actual production for the given year should be `None`.
- If only one of the farmed or wild caught data points is missing for the given `year` for this country, then the actual production should just be the existing value. In other words, treat `None` as 0 in this case.

### Problem 1d: Production need

Document and implement the `calc_production_need` method that takes `self` and a `year` and updates the `self.need` dictionary with an entry for the country's **production need** to feed the country's population for the given `year`. If either _population_ or _consumption_ is missing for the given `year` and country, then the need value should be `None`.

production need
: The product (multiplication) of the _population_ and _consumption_ divided by 1000 for the country in the given year.

We divide by 1000 to correct for different units: _consumption_ is given in kilograms per person, but _production_ is given in metric tons (1000 kg).

### Problem 1e: Calculate

Document and implement the `calculate` method that takes `self` and updates the actual production and the production need for each year in `self.years`. Call `calc_actual_production` and `calc_production_need` for each year. This method does not return anything.

## Problem 2: `Fishing` class

### Problem 2a: Initialization

Document and implement the `__init__` method that takes `self` and a `filename` and opens the file `filename`, uses `csv.DictReader` to read the file, and initializes the following fields:

- `self.min_year`: The minimum year in the entire dataset.
- `self.max_year`: The maximum year in the entire dataset.
- `self.countries`: A dictionary mapping each `country code` in the dataset to a `Country` object with all the country's data loaded.

### Problem 2b: Total production need

So, now that we've done all that work, how much fish will the **entire world** need to produce 50 years from now?

Document and implement the `total_production_need` method that takes `self and an `int` number of `years_to_predict` and returns a single number: how many metric tonnes of fish will the world need to produce `years_to_predict` years from now? For each country code in `self.countries`:

- Calculate the needed production using the country's `calculate` method. (This doesn't return anything, just updates the `Country` object.)
- Predict the production need for `years_to_predict` years from now using the country's `predict_need` method (already implemented for you).
- Extract the last predicted production need, such as `prediction[1][-1]`.

Then, return the sum of all the predicted production needs.

Finally, let's run the program! At the bottom of `fishing.py`, edit the `__main__` conditional block to create an instance of the `Fishing` class with `small.csv` as the file. Save the instance in a variable called `data` before calling `total_production_need` for 50 years. `%run fishing.py` should report no doctest failures and a global production need of approximately 13243690.76...

## Problem 3: Visualizations

### Problem 3a: Production vs. need

Document and implement the `plot_production_vs_need` method in the `Country` class that takes `self` and plots the country's actual production versus its production need (not consumption) over time. To access this data for each country, calls to `calc_actual_production` and `calc_production_need` are required to populate those fields before accessing the `self.production` and `self.need` dictionaries.

- Produce two lists, one for the actual production and one for the production need.
- Plot the two lists of data on a line plot, making two calls to `plt.plot` with the same `years` as the x-axis values. In each `plot` call:
  - Add a label for each line by specifying the `label` parameter.
  - Due to missing y-axis values, specify `marker='s'`.

Additionally, the plot should have the following attributes:

- "Year" as the x-axis label
- "Metric Tonnes" as the y-axis label
- "Production vs. Need for `self.name`" as the title
- A legend

Finally, call `plt.savefig(str(self.name) + "-prod-vs-need.png")` to save the plot as a PNG image and uncomment the lines of code in the `__main__` block to call your method. The result should match the following plot.

```{code-cell} python
:tags: [remove-input]

import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from IPython.display import HTML, display

df = pd.read_csv("small.csv")
usa = (
    df[df["country code"] == "USA"]
    .drop(columns=["country", "country code"])
    .set_index("measure").rename_axis(None, axis="index")
    .apply(pd.to_numeric)
    .transpose()
)
usa["production"] = usa["farmed"] + usa["wild caught"]
usa["need"] = (usa["population"] * usa["consumption"]) / 1000
ax = usa[["production", "need"]].plot(
    marker="s",
    xlabel="Year",
    ylabel="Metric Tonnes",
    title="Production vs. Need for United States"
)

buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_str = base64.b64encode(buf.read()).decode("utf-8")
plt.close()

display(HTML(f'<img src="data:image/png;base64,{img_str}" alt="Line plot showing production and need for the United States from 1995 to 2000. Production alternates between higher and lower years but shows a downward trend from about 5.8 million metric tonnes in 1995 to 5.5 million metric tonnes in 2000. Need starts at 5.8 million metric tonnes in 1995, dips to 5.7 million metric tonnes in 1997, but then grows to 6.2 million metric tonnes in 2000 with a missing data point for 1998.">'))
```

### Problem 3b: Pause and think

Pause for a few minutes to think about the plot above. Answer the following questions in `answers.txt`. When did the United States' need surpass its production? What's missing from the data we gave you that would help explain why the United States was still able to consume more fish than it produced?

### Problem 3c: Linear prediction

Let's use the given `predict_need` method to plot a linear prediction for US production need 50 years from now. Simply uncomment the following line of code in the `__main__` block.

```python
plot_linear_prediction(usa)
```

Running your program should then result in no doctest failures and a new PNG image, `United-States-need-prediction.png`.

```{code-cell} python
:tags: [remove-input]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from IPython.display import HTML, display

df = pd.read_csv("small.csv")
usa = (
    df[df["country code"] == "USA"]
    .drop(columns=["country", "country code"])
    .set_index("measure").rename_axis(None, axis="index")
    .apply(pd.to_numeric)
    .transpose()
)
valid_need = (usa["population"] * usa["consumption"]).dropna() / 1000
years = valid_need.index.values.astype(int)
needs = valid_need.values
ax = pd.Series(needs, index=years).plot(
    marker="s",
    linestyle="",
    label="data",
    xlabel="Year",
    ylabel="Metric Tonnes",
    title="Predicted Production Need for United States",
    legend=True
)
m, b = np.polyfit(years, needs, 1)
x = np.arange(years.min(), years.max() + 51)
pd.DataFrame({"best-fit prediction": m * x + b}, index=x).plot(ax=ax, linestyle="--")

buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_str = base64.b64encode(buf.read()).decode("utf-8")
plt.close()

display(HTML(f'<img src="data:image/png;base64,{img_str}" alt="Linear prediction plot for United States seafood production need. The plot shows historical data points and a dashed best-fit line projecting the need out to 50 years in the future, indicating a steady increase from 0.6 million metric tonnes in 2000 to 1.1 million metric tonnes in 2050.">'))
```

## Running on `large.csv`

So far, we've been testing our program with `small.csv`. Let's try running the program on `large.csv`. Edit your `Fishing` `data` to read the file `large.csv`. Then, at the very end of your program, add a print statement to display the `total_production_need`. `%run fishing.py` should print:

```text
Metric tonnes of fish needed to be produced in 50 years: 245637243.2239474
```

## Code quality

Run our linter (automated code style checker) in the Python console with the expression `!flake8`. Edit the file and save your changes after addressing all reported issues. A successful `!flake8` run will print nothing when there are no linting issues to report.

```ipython
!flake8
```

Then, review our [style guide](../../style-guide.md).

> [!important]
> All methods must include descriptive docstrings and follow the course style guide.

## Collaboration

If you discuss an assignment with one or more classmates, **you must specify with whom you collaborated in a comment at the bottom of your submission**. You may discuss with as many classmates as you like, but you must cite all of them in your work. Note that you may not collaborate in a way that is prohibited, even if you cite the collaboration.

**At the bottom of your `fishing.py` and `answers.txt` files**, state which students or other people (besides the course staff) helped you with the assignment, or that no one did.

## Submission

Submit `fishing.py` and `answers.txt` on Gradescope under the assignment **Homework: Fishing Analysis**.
