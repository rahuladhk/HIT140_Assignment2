# FIFA World Cup 2026 – Task 1: Player Goals by Position

## Research Question

**On average, did forwards score more goals per game than midfielders in the FIFA World Cup 2026?**

This analysis investigates whether there was a statistically significant difference in goals per game between forwards and midfielders during the FIFA World Cup 2026.

---

## Objective

The objective of this task is to:

1. Compare the average goals per game scored by forwards and midfielders.
2. Calculate descriptive statistics for both player groups.
3. Calculate 95% confidence intervals for the group means.
4. Perform a statistical hypothesis test to determine whether the difference is significant.
5. Visualise the distribution of goals per game using a box plot.
6. Provide a conclusion supported by the statistical results.

---

## Dataset

The analysis uses a FIFA World Cup 2026 player-match dataset stored as:

```text
CSV_data/WC_2026.csv
```

The original dataset contains:

* **5,359 player-match records**
* **1,245 unique players**
* **104 unique matches**
* **124 columns**

Because the dataset contains multiple records for players across different matches, the data is aggregated to produce **one record per player** before calculating goals per game.

### Player-level data

After aggregation and filtering:

* **295 forwards**
* **328 midfielders**
* **623 players in total**

Players with zero recorded appearances are excluded from the analysis.

---

## Data Preparation

The following steps are performed before statistical analysis:

1. Load the CSV dataset using pandas.
2. Check that the required columns are present.
3. Convert goals and match appearances to numeric values.
4. Check for duplicate player-match records.
5. Aggregate match-level records by player.
6. Sum each player's total goals.
7. Sum each player's recorded match appearances.
8. Remove players with zero appearances.
9. Select only players classified as:

   * Forward
   * Midfielder
10. Calculate goals per game.

The calculation used is:

```text
Goals per game = Total goals / Matches played
```

This produces one `goals_per_game` value for each player.

---

## Statistical Method

### Descriptive Statistics

The following statistics are calculated separately for forwards and midfielders:

* Number of players
* Mean
* Median
* Standard deviation
* Minimum
* Maximum

### Confidence Intervals

A **95% confidence interval** is calculated for the mean goals per game for each position group.

### Hypothesis Test

A **Welch independent two-sample t-test** is used to compare the mean goals per game of forwards and midfielders.

Welch's t-test was selected because it does not assume that the two groups have equal variances.

#### Null Hypothesis (H₀)

> There is no difference in the mean goals per game between forwards and midfielders.

#### Alternative Hypothesis (H₁)

> Forwards have a higher mean goals per game than midfielders.

The significance level is:

```text
α = 0.05
```

A p-value below 0.05 is considered statistically significant.

---

## Data Validation and Tests

Several checks are performed by the analysis script before the statistical calculations.

### Test 1 – Dataset Loading

Confirms that the CSV file can be loaded successfully.

Expected result:

```text
Original dataset shape:
(5359, 124)
```

### Test 2 – Unique Player and Match Counts

Checks the number of unique players and matches in the dataset.

Expected result:

```text
Unique players: 1245
Unique matches: 104
```

### Test 3 – Duplicate Player-Match Records

Checks whether the same player has been recorded more than once for the same match.

Expected result:

```text
Duplicate player-match records: 0
```

### Test 4 – Player Aggregation

Confirms that multiple match-level records are correctly combined into one record per player.

For example, a player appearing in five matches should have:

```text
matches_played = 5
```

and their goals should be summed across those matches.

### Test 5 – Zero-appearance Players

Players with zero recorded appearances are excluded so that non-participating players do not distort the goals-per-game calculation.

### Test 6 – Position Filtering

Only players classified as `Forward` or `Midfielder` are included in the statistical comparison.

### Test 7 – Goals-per-game Calculation

For every included player:

```text
goals_per_game = total_goals / matches_played
```

Players with zero appearances are removed before this calculation.

### Test 8 – Statistical Significance

Welch's t-test is used to determine whether the observed difference between the two groups is statistically significant.

---

## Results

### Descriptive Statistics

| Position   | Players |       Mean | Median | Std. Dev. | Minimum | Maximum |
| ---------- | ------: | ---------: | -----: | --------: | ------: | ------: |
| Forward    |     295 | **0.1299** | 0.0000 |    0.2515 |  0.0000 |  1.4000 |
| Midfielder |     328 | **0.0776** | 0.0000 |    0.1794 |  0.0000 |  1.0000 |

Forwards scored approximately:

```text
0.1299 goals per game
```

while midfielders scored:

```text
0.0776 goals per game
```

The difference between the means is approximately:

```text
0.0523 goals per game
```

---

## 95% Confidence Intervals

| Position   |   Mean | 95% Confidence Interval |
| ---------- | -----: | ----------------------: |
| Forward    | 0.1299 |         0.1012 – 0.1586 |
| Midfielder | 0.0776 |         0.0582 – 0.0971 |

---

## Welch's t-test

The statistical test produced:

```text
t-statistic = 2.9588
Degrees of freedom = 525.79
p-value = 0.003228
Significance level = 0.05
```

Since:

```text
0.003228 < 0.05
```

the null hypothesis is rejected.

There is statistically significant evidence that the mean goals per game differs between forwards and midfielders.

The observed difference is also in the direction specified by the research question: forwards have the higher mean.

---

## Conclusion

**Yes. Forwards scored more goals per game on average than midfielders in the FIFA World Cup 2026 dataset.**

Forwards recorded an average of **0.1299 goals per game**, compared with **0.0776 goals per game** for midfielders.

Welch's independent two-sample t-test produced a p-value of **0.003228**, which is below the 0.05 significance level. Therefore, the difference is statistically significant.

The results provide evidence supporting the conclusion that forwards scored more goals per game than midfielders.

---

## Visualisation

The analysis produces a box plot comparing the distribution of goals per game between forwards and midfielders.

The generated file is:

```text
task1_goals_per_game_boxplot.png
```

The box plot helps show the distribution, spread, and potential differences between the two player groups.

---

## Output Files

Running the analysis creates the following files:

```text
task1_player_level_data.csv
task1_goals_per_game_boxplot.png
```

### `task1_player_level_data.csv`

Contains the cleaned player-level dataset used for the statistical analysis.

### `task1_goals_per_game_boxplot.png`

Contains the box plot comparing forwards and midfielders.

---

## Requirements

The analysis uses Python and the following libraries:

* Python 3.x
* pandas
* numpy
* matplotlib
* mpmath

Install the required packages with:

```powershell
python -m pip install pandas numpy matplotlib mpmath
```

---

## How to Run

Open PowerShell or a terminal in the project directory:

```powershell
cd C:\Users\Eran\HIT140_Assignment2\Eran_Task1
```

Then run:

```powershell
python Task1_analysis.py
```

The program will:

1. Load the World Cup dataset.
2. Validate the data.
3. Aggregate player-match records.
4. Filter the required player positions.
5. Calculate goals per game.
6. Calculate descriptive statistics.
7. Calculate 95% confidence intervals.
8. Perform Welch's independent two-sample t-test.
9. Display the research conclusion.
10. Generate the cleaned dataset and box plot.

---

## Important Limitation

Goals per game in this analysis is based on **matches/appearances**, rather than minutes played.

For example, a player who appeared for 90 minutes and a player who appeared for only a short period in a match are both counted as having one appearance.

Therefore, this analysis measures:

> **Goals per appearance/game**

rather than:

> **Goals per 90 minutes**

A goals-per-90 analysis could provide additional insight into scoring efficiency while accounting for playing time, but it would answer a different research question.

---

## Reproducibility

All calculations are performed programmatically in:

```text
Task1_analysis.py
```

The analysis can therefore be rerun using the same dataset to reproduce the reported statistics and visualisation.

---

## Summary

| Item                   | Result                                                  |
| ---------------------- | ------------------------------------------------------- |
| Research question      | Do forwards score more goals per game than midfielders? |
| Forward players        | 295                                                     |
| Midfielder players     | 328                                                     |
| Forward mean           | **0.1299**                                              |
| Midfielder mean        | **0.0776**                                              |
| Difference             | **0.0523**                                              |
| t-statistic            | **2.9588**                                              |
| Degrees of freedom     | **525.79**                                              |
| p-value                | **0.003228**                                            |
| Significance level     | **0.05**                                                |
| Statistical conclusion | **Reject H₀**                                           |
| Overall conclusion     | **Forwards scored more goals per game**                 |
