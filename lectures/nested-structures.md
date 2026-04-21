---
exports:
  - format: typst
    template: ./
    id: nested-structures-handout
downloads:
  - id: nested-structures-handout
    title: Handout
---

# Nested Structures

Nested lists and nested dictionaries organize data into a hierarchical format. Programmers often have to choose between different nested representations depending on the problem at hand.

```python
food_list = [
    ["Agua Verde", "Montlake", 4.3],
    ["Bangrak", "Belltown", 4.8],
    ["Crackle Mi", "Ballard", 4.4]
]

# Accessing Bangrak's rating requires knowing the exact indices:
food_list[1][2]
```

```python
food_dict = {
    "Agua Verde": {"Neighborhood": "Montlake", "Rating": 4.3},
    "Bangrak": {"Neighborhood": "Belltown", "Rating": 4.8},
    "Crackle Mi": {"Neighborhood": "Ballard", "Rating": 4.4}
}

# Accessing Bangrak's rating uses meaningful keys:
food_dict["Bangrak"]["Rating"]
```

## Problem solving strategy

Use these iterative development strategies to break down complex problems:

1. **Relate inputs to outputs**: What data types are you given? What data types do you need to return?
1. **Solve a subproblem**: Can you solve a smaller problem first? What about the nested, inner structure?
1. **Combine subproblem solutions**: After working on the subproblem, how can you address the larger problem?

> [!tip]
> When you open an exam or assignment and feel stumped, don't try to write the entire solution at once. Identify a small piece of the logic you do understand and write that first! Where have you seen similar examples or practice problems before?

## Practice: Olympic grouping

Imagine you are given a file `olympics.txt` containing each 2026 Winter Olympics discipline and its corresponding location:

    Ice Hockey: Milan
    Cross-Country Skiing: Tesero
    Speed Skating: Milan
    Alpine Skiing: Cortina
    Freestyle Skiing: Livigno
    Figure Skating: Milan

Create a dictionary where each location is a key. The value for a location should be a list of all Olympic disciplines taking place at that location. For example, the location "Milan" should evaluate to `['Ice Hockey', 'Speed Skating', 'Figure Skating']`.

## Practice: Triply-nested lists

Consider a triply-nested list representing a grid of **color pixels**. Each innermost list contains Red, Green, and Blue (RGB) values. For each pixel, set all three color values to the highest of that pixel's three RGB values.

```python
pixel_grid = [
    [[128, 50, 20], [50, 50, 60]],
    [[75, 67, 90], [42, 240, 100]]
]
```

## Practice: RNA translation

RNA sequences consist of the letters A, U, C, and G. Each triplet of nucleotides translates to an amino acid based on a known mapping.

```python
rna_mapping = {
    "AUG": "Methionine",
    "UGC": "Cysteine",
    "UCU": "Serine"
}
```

Use a `for` loop, `range`, and string slicing to translate an RNA sequence into a list of amino acids. Triplets that don't match any known mapping are ignored.

```python
sequence_1 = "AUGCUCAUG"
# ['Methionine', 'Methionine']
```

```python
sequence_2 = "ACCUUUAUGAUUUGCUCUUUUUGCUCU"
# ['Methionine', 'Cysteine', 'Serine', 'Cysteine', 'Serine']
```
