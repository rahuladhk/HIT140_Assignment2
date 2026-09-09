# HIT140 Assignment 2 – FIFA World Cup 2026 Data Analysis

## Overview

This repository contains the group work for **HIT140 Assignment 2**.

The project analyses FIFA World Cup 2026 data using Python and statistical/data-analysis techniques. The assignment consists of four separate analytical tasks, with each group member responsible for an individual task.

The overall aim is to use appropriate data preparation, statistical analysis, visualisation, and interpretation techniques to investigate different aspects of FIFA World Cup 2026 player and match performance.

---

## Group

**Darwin Group 59**

### Group Members and Tasks

| Task   | Member          | Analysis                                       |
| ------ | --------------- | ---------------------------------------------- |
| Task 1 | Eran (S397628)  | Player goals by position                       |
| Task 2 | Avaya (S397651) | Possession vs Goals                            |
| Task 3 | Rahul (S397719) | Discipline and yellow cards by player position |
| Task 4 | Biraj (S397466) | Substitutions and goals                        |

---

# Project Structure

```text
HIT140_Assignment2/
│
├── Eran_Task1/
│   ├── CSV_data/
│   ├── Task1_analysis.py
│   ├── task1_player_level_data.csv
│   ├── task1_goals_per_game_boxplot.png
│   └── README.md
│
├── TASK 2 - AVAYA MANANDHAR/
│   ├── data/
│   └── Task2_Possession_vs_Goals.ipynb
│
├── Task-3/
│   ├── Discipline_Compare.py
│   ├── Discipline_csv.py
│   ├── FIFA_2026_Discipline.csv
│   ├── wc2026_efi.csv
│   └── README.txt
│
└── Task-4 - Biraj Shrestha/
    ├── data/
    ├── task4_substitutions_goals.ipynb
    ├── goals_by_substitution_group.png
    └── subs_vs_goals_scatter.png
```

---

# Tasks

## Task 1 – Player Goals by Position

### Research Question

> **On average, did forwards score more goals per game than midfielders in the FIFA World Cup 2026?**

Task 1 compares the scoring performance of forwards and midfielders.

The analysis:

* Loads the FIFA World Cup 2026 player-match dataset.
* Aggregates match-level records into player-level data.
* Calculates each player's goals per game.
* Separates players into forwards and midfielders.
* Calculates descriptive statistics.
* Calculates 95% confidence intervals.
* Performs a **Welch independent two-sample t-test**.
* Produces a box plot comparing the two groups.

### Main Result

The analysis found:

| Position   | Players | Mean Goals/Game |
| ---------- | ------: | --------------: |
| Forward    |     295 |          0.1299 |
| Midfielder |     328 |          0.0776 |

The difference in means was approximately **0.0523 goals per game**.

Welch's t-test produced:

```text
t-statistic = 2.9588
degrees of freedom = 525.79
p-value = 0.003228
α = 0.05
```

Since:

```text
0.003228 < 0.05
```

the null hypothesis was rejected.

### Conclusion

There is statistically significant evidence that forwards scored more goals per game than midfielders in the analysed FIFA World Cup 2026 dataset.

More details are available in:

```text
Eran_Task1/README.md
```

---

## Task 2 – Possession vs Goals

Task 2 investigates the relationship between **team possession and goals scored**.

The analysis is implemented in:

```text
TASK 2 - AVAYA MANANDHAR/Task2_Possession_vs_Goals.ipynb
```

The notebook contains the data preparation and statistical analysis required to investigate whether teams with greater possession tend to score more goals.

The task uses Python-based data analysis and visualisation techniques to explore the relationship between possession and scoring performance.

---

## Task 3 – Discipline and Yellow Cards

Task 3 investigates disciplinary statistics in the FIFA World Cup 2026 dataset, with particular focus on yellow cards received by different player positions.

The task uses:

```text
Task-3/
├── Discipline_csv.py
├── Discipline_Compare.py
├── wc2026_efi.csv
└── FIFA_2026_Discipline.csv
```

### Data Processing

`Discipline_csv.py` processes the raw dataset:

```text
wc2026_efi.csv
```

and creates a filtered dataset:

```text
FIFA_2026_Discipline.csv
```

containing the required columns for the analysis.

### Analysis

`Discipline_Compare.py` then analyses the processed dataset and compares the number of yellow cards received by different player positions, including defenders and forwards.

---

## Task 4 – Substitutions vs Goals

Task 4 investigates the relationship between **player substitutions and goals**.

The analysis is contained in:

```text
Task-4 - Biraj Shrestha/task4_substitutions_goals.ipynb
```

The task includes visualisations such as:

```text
goals_by_substitution_group.png
subs_vs_goals_scatter.png
```

These visualisations are used to explore how substitution-related factors relate to goals scored.

---

# Data Analysis Workflow

Across the four tasks, the project generally follows the following workflow:

```text
Raw FIFA World Cup 2026 Data
            │
            ▼
      Data Preparation
            │
            ▼
      Data Validation
            │
            ▼
    Variable Selection
            │
            ▼
   Statistical Analysis
            │
            ▼
      Visualisation
            │
            ▼
 Interpretation of Results
            │
            ▼
        Conclusion
```

Each task focuses on a different research question while using the FIFA World Cup 2026 datasets as the underlying source of information.

---

# Technologies Used

The project primarily uses **Python** for data analysis.

Depending on the task, the project uses tools and libraries including:

* Python 3.x
* pandas
* NumPy
* matplotlib
* mpmath
* Jupyter Notebook

The exact dependencies may vary between individual tasks.

---

# Statistical Methods

Different statistical techniques are used depending on the research question.

### Descriptive Statistics

Used to summarise datasets and compare groups using measures such as:

* Mean
* Median
* Standard deviation
* Minimum
* Maximum
* Sample size

### Confidence Intervals

Task 1 calculates **95% confidence intervals** for the mean goals-per-game values of forwards and midfielders.

### Welch's Independent Two-Sample t-Test

Task 1 uses Welch's t-test to compare the mean goals-per-game values of forwards and midfielders.

Welch's test was selected because it does not require the two groups to have equal variances.

The significance level used is:

```text
α = 0.05
```

A p-value below 0.05 is interpreted as statistically significant.

### Visualisation

Visualisations are used throughout the project to make patterns and relationships easier to interpret.

Examples include:

* Box plots
* Scatter plots
* Group comparisons

---

# Installation

Make sure Python 3.x is installed.

For Task 1, the required packages can be installed using:

```bash
python -m pip install pandas numpy matplotlib mpmath
```

For notebook-based tasks, Jupyter Notebook or JupyterLab may also be required:

```bash
python -m pip install jupyter
```

---

# Running the Analyses

## Task 1

Navigate to the Task 1 directory:

```bash
cd Eran_Task1
```

Run:

```bash
python Task1_analysis.py
```

The program will:

1. Load the FIFA World Cup 2026 dataset.
2. Validate the input data.
3. Aggregate player-match records.
4. Filter forwards and midfielders.
5. Calculate goals per game.
6. Calculate descriptive statistics.
7. Calculate confidence intervals.
8. Perform Welch's t-test.
9. Display the statistical results.
10. Generate the output dataset and visualisation.

---

## Task 2

Open:

```text
TASK 2 - AVAYA MANANDHAR/Task2_Possession_vs_Goals.ipynb
```

Run the notebook cells sequentially.

---

## Task 3

Navigate to:

```text
Task-3/
```

The raw data can first be processed using:

```bash
python Discipline_csv.py
```

The resulting filtered dataset can then be analysed using:

```bash
python Discipline_Compare.py
```

---

## Task 4

Open:

```text
Task-4 - Biraj Shrestha/task4_substitutions_goals.ipynb
```

Run the notebook cells sequentially to reproduce the analysis and visualisations.

---

# Reproducibility

The analyses are designed to be reproducible from the included scripts, notebooks, and datasets.

Where applicable, generated files are also included in the repository so that the results can be inspected without rerunning the complete analysis.

For example, Task 1 includes:

```text
task1_player_level_data.csv
task1_goals_per_game_boxplot.png
```

---

# Important Notes and Limitations

The interpretation of results depends on how the FIFA World Cup 2026 datasets record player and match information.

For example, Task 1 calculates goals per game using recorded player appearances:

```text
Goals per game = Total goals / Matches played
```

This is therefore a measure of **goals per appearance/game**, rather than goals scored per 90 minutes.

A player appearing briefly in a match and a player playing the entire match are both counted as having one appearance.

Consequently, the results should not be interpreted as a direct measure of scoring efficiency per minute played.

Other tasks may have their own assumptions and limitations, which are documented within their respective folders.

---

# Repository Organisation

Each task is kept in a separate directory so that:

* Individual analyses remain independent.
* Each group member's work can be identified clearly.
* Data files and generated outputs remain organised.
* Scripts and notebooks can be reproduced independently.
* The final repository provides a complete record of the group's analytical work.

---

# Summary

This repository contains four complementary analyses of FIFA World Cup 2026 data:

1. **Player Goals by Position**
   Examines whether forwards score more goals per game than midfielders.

2. **Possession vs Goals**
   Investigates the relationship between team possession and goals scored.

3. **Discipline and Yellow Cards**
   Compares disciplinary outcomes across player positions.

4. **Substitutions vs Goals**
   Investigates the relationship between substitutions and scoring outcomes.

Together, the four tasks demonstrate the use of **data cleaning, statistical analysis, hypothesis testing, visualisation, and interpretation** to investigate football-related research questions using Python.

---

## Repository

**GitHub:**
https://github.com/rahuladhk/HIT140_Assignment2
