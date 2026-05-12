---
exports:
  - format: typst
    template: ./
    id: csv-file-processing-handout
downloads:
  - id: csv-file-processing-handout
    title: Handout
---

# CSV File Processing

So far, we have read in standard **CSV (Comma Separated Values)** files where every line contains identically formatted data. However, many real-world datasets include a **header row**. The first line of the file contains column names rather than actual data, and the remaining lines contain the data. For example, in `games.csv`, we had to skip the header row to read the actual NFL game data!

```csv
schedule_season,schedule_date,team_home,team_away,score_home,score_away
2018,2019-01-06,Chicago Bears,Philadelphia Eagles,15,16
2022,2023-01-08,Atlanta Falcons,Tampa Bay Buccaneers,30,17
1981,1981-10-11,San Francisco 49ers,Dallas Cowboys,45,14
```

## `csv.DictReader`

To handle CSV files with headers efficiently, we can use the `DictReader` class from Python's built-in `csv` package. `csv.DictReader(f)` takes a file handle and creates an object that maps information from a CSV file into a sequence of dictionaries:

- Each row of data becomes a separate dictionary.
- The column headers (from the first row) become the **keys** for each dictionary.
- The actual row data becomes the **values** for each respective key.

To use it, we must first import the `csv` package:

```python
import csv

result = []
with open("data/games.csv") as f:
    reader = csv.DictReader(file)
    for row in reader:
        result.append(row)
```

> [!warning]
> `DictReader` is an iterator object: after looping through all the rows once using a `for` loop, we consume the iterator and cannot iterate through it again from the beginning without reopening the file and creating a new reader.

The `DictReader` object has a few useful attributes that you can access while processing your file:

- `reader.line_num`: Returns the current line number in the CSV file (at its current state).
- `reader.fieldnames`: Returns a list of the parsed column headers (the keys).

## Practice: NFL DictReader

After running the above code to add each row to the `result`, which expression will run without error?

    result["schedule_date"]
    result["team_home"][0]
    result["2023-01-08"]
    result[0]["2019-01-06"]
    result[1]["score_home"] = 24
