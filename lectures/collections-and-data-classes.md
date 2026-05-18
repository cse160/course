---
exports:
  - format: typst
    template: ./
    id: collections-and-data-classes-handout
downloads:
  - id: collections-and-data-classes-handout
    title: Handout
---

# Collections and Data Classes

Python provides many built-in data structures like lists, dictionaries, and tuples. However, sometimes we need more specialized or structured ways to represent and process data. Python's built-in `collections` and `dataclasses` modules provide powerful tools for these scenarios.

## `collections.Counter`

When we want to count the occurrences of elements in a list, we typically use a dictionary. For example, let's figure out how many Olympic disciplines are hosted in each location from `olympics.txt`.

```python
with open("data/olympics.txt") as f:
    locations = []
    for line in f:
        # Example line: "Ice Hockey: Milan"
        location = line.strip().split(": ")[1]
        locations.append(location)

counts = {}
for loc in locations:
    if loc not in counts:
        counts[loc] = 0
    counts[loc] += 1
print(counts)
```

The `Counter` class from the `collections` module simplifies this common pattern. When we pass a list to `Counter`, it automatically counts the frequency of each element for us.

```python
from collections import Counter

counts = Counter(locations)
print(counts)
print(counts.most_common(2))
```

## `collections.defaultdict`

Earlier, we created a dictionary grouping each location to a list of its Olympic disciplines.

```python
disciplines_by_location = {}
with open("data/olympics.txt") as f:
    for line in f:
        discipline, location = line.strip().split(": ")
        if location not in disciplines_by_location:
            disciplines_by_location[location] = []
        disciplines_by_location[location].append(discipline)
```

We can simplify the process of initializing empty lists for new keys using `defaultdict` from the `collections` module. When you access a key that doesn't exist, `defaultdict` automatically creates it using the function you provided (like `list` for an empty list or `int` for 0).

## Practice: Grouping with `defaultdict`

Which line of code correctly initializes `disciplines_by_location` using a `defaultdict` so that we no longer need the `if` statement inside the `for` loop?

    disciplines_by_location = defaultdict(list)
    disciplines_by_location = defaultdict([])
    disciplines_by_location = defaultdict(int)
    disciplines_by_location = defaultdict(list())

## Data classes

When processing structured files like CSVs, dictionaries are useful but we've learned that classes can be a better alternative if we want to define methods that act on the structured data. But we've seen that classes in Python require quite a substantial boilerplate (template) code. The `@dataclass` decorator automatically generates dunder methods like `__init__`, `__repr__` and `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class Game:
    season: int
    date: str
    team_home: str
    team_away: str
    score_home: int
    score_away: int

my_game = Game(2024, "2024-10-20", "Washington Commanders", "Carolina Panthers", 40, 7)
my_game
```

We can combine `dataclasses` with our file processing skills.

```python
import csv

games = []
with open("data/games.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        game = Game(
            season=int(row["schedule_season"]),
            date=row["schedule_date"],
            team_home=row["team_home"],
            team_away=row["team_away"],
            score_home=int(row["score_home"]),
            score_away=int(row["score_away"])
        )
        games.append(game)

games
```

## Practice: NFL Dataclasses

After defining the `Game` dataclass and creating the `my_game` instance above, which expression will raise an error?

    my_game["score_home"]
    my_game.score_home
    my_game.season == 2024
    my_game.team_home = "Seattle Seahawks"

## Sorting by attribute

One of the major benefits of using dataclasses (and objects in general) is how nicely they work with Python's `sorted` function. Just as we used `operator.itemgetter` to sort dictionaries by a specific key, we can use `operator.attrgetter` to sort objects by a specific attribute.

```python
from operator import attrgetter

# Sort the games from lowest home score to highest home score
sorted_games = sorted(games, key=attrgetter("score_home"))
sorted_games[-1].score_home
```
