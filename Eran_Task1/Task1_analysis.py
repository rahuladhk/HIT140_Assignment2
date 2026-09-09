# Starting with all the important imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# ============================================================
# TASK 1 - PLAYER GOALS BY POSITION
# Question:
# On average, did forwards score more goals per game
# than midfielders in the FIFA World Cup 2026?
# ============================================================


# 
# Loading the dataset (CSV_File)
# 

DATA_FILE = "CSV_data/WC_2026.csv"

df = pd.read_csv(DATA_FILE)

print("=" * 70)
print("TASK 1 - PLAYER GOALS BY POSITION")
print("=" * 70)

print("\nOriginal dataset shape:")
print(df.shape)

print("\nUnique players:", df["player_id"].nunique())
print("Unique matches:", df["match_id"].nunique())


# 
# Checking and verifying required columns
# 

required_columns = [
    "player_id",
    "player_name",
    "position",
    "match_id",
    "goals",
    "matches_played"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# 
# Converting relevant columns to numeric
# 

df["goals"] = pd.to_numeric(
    df["goals"],
    errors="coerce"
)

df["matches_played"] = pd.to_numeric(
    df["matches_played"],
    errors="coerce"
)

df["goals"] = df["goals"].fillna(0)
df["matches_played"] = df["matches_played"].fillna(0)


# 
# Checking for duplicate player-match records
# 

duplicate_records = df.duplicated(
    subset=["player_id", "match_id"]
).sum()

print("\nDuplicate player-match records:", duplicate_records)

if duplicate_records > 0:
    raise ValueError(
        "Duplicate player-match records detected. "
        "Check the dataset before continuing."
    )


# 
# Aggregate player-match records
# 
#
# The dataset contains multiple rows for the same player,
# because each row represents a player in a particular match.
#
# matches_played is 1 when the player appeared and 0 when
# the player was listed but did not play.
#
# Therefore:
#     total_goals = sum of goals across matches
#     matches_played = sum of match appearances
# 

player_data = (
    df.groupby(
        [
            "player_id",
            "player_name",
            "position"
        ],
        as_index=False
    )
    .agg(
        total_goals=("goals", "sum"),
        matches_played=("matches_played", "sum")
    )
)


# 
# Removing players with no recorded appearances
# 

player_data = player_data[
    player_data["matches_played"] > 0
].copy()


# 
# Keeping only forwards and midfielders
# 

player_data = player_data[
    player_data["position"].isin(
        ["Forward", "Midfielder"]
    )
].copy()


# 
# Calculating goals per game
# 

player_data["goals_per_game"] = (
    player_data["total_goals"]
    / player_data["matches_played"]
)


# 
# Displaying player-level data
# 

print("\n" + "=" * 70)
print("PLAYER-LEVEL DATA")
print("=" * 70)

print("\nNumber of players included:", len(player_data))

print("\nPlayers by position:")
print(
    player_data["position"]
    .value_counts()
)

print("\nFirst 10 player records:")

print(
    player_data[
        [
            "player_id",
            "player_name",
            "position",
            "total_goals",
            "matches_played",
            "goals_per_game"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


# 
# Descriptive statistics
# 

summary = (
    player_data
    .groupby("position")["goals_per_game"]
    .agg(
        count="count",
        mean="mean",
        median="median",
        std="std",
        min="min",
        max="max"
    )
)

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

print(
    summary.to_string(
        float_format=lambda x: f"{x:.4f}"
    )
)


# 
# 95% confidence intervals
# 
#
# A large-sample 95% confidence interval is calculated using
# the standard normal critical value of 1.96.
#
# CI = mean +/- 1.96 * standard error
# 

def confidence_interval(data, confidence=0.95):

    data = np.asarray(data, dtype=float)

    n = len(data)

    mean = np.mean(data)

    std = np.std(
        data,
        ddof=1
    )

    standard_error = std / math.sqrt(n)

    critical_value = 1.96

    margin = critical_value * standard_error

    lower = mean - margin
    upper = mean + margin

    return lower, upper


print("\n" + "=" * 70)
print("95% CONFIDENCE INTERVALS")
print("=" * 70)

for position in ["Forward", "Midfielder"]:

    values = player_data.loc[
        player_data["position"] == position,
        "goals_per_game"
    ]

    lower, upper = confidence_interval(values)

    print(
        f"{position}: "
        f"mean = {values.mean():.4f}, "
        f"95% CI = ({lower:.4f}, {upper:.4f})"
    )


# 
# Preparing data for Welch's t-test
# 

forwards = player_data.loc[
    player_data["position"] == "Forward",
    "goals_per_game"
].to_numpy()

midfielders = player_data.loc[
    player_data["position"] == "Midfielder",
    "goals_per_game"
].to_numpy()


forward_mean = np.mean(forwards)
midfielder_mean = np.mean(midfielders)

forward_variance = np.var(
    forwards,
    ddof=1
)

midfielder_variance = np.var(
    midfielders,
    ddof=1
)

forward_n = len(forwards)
midfielder_n = len(midfielders)


# 
# Welch's independent two-sample t-test
# 
#
# H0:
# There is no difference between the mean goals per game
# of forwards and midfielders.
#
# H1:
# Forwards have a higher mean goals per game than midfielders.
#
# The test statistic is:
#
# t = (mean1 - mean2) /
#     sqrt(s1^2/n1 + s2^2/n2)
#
# Welch's method does not assume equal variances.
# 

standard_error_difference = math.sqrt(
    (forward_variance / forward_n)
    +
    (midfielder_variance / midfielder_n)
)

t_stat = (
    forward_mean - midfielder_mean
) / standard_error_difference


# Welch-Satterthwaite degrees of freedom

numerator = (
    (forward_variance / forward_n)
    +
    (midfielder_variance / midfielder_n)
) ** 2

denominator = (
    (
        (forward_variance / forward_n) ** 2
    ) / (forward_n - 1)
) + (
    (
        (midfielder_variance / midfielder_n) ** 2
    ) / (midfielder_n - 1)
)

degrees_of_freedom = numerator / denominator


# 
# Calculating two-tailed p-value
# 
#
# The t probability is calculated using the
# regularised incomplete beta function from mpmath.
# 

try:

    import mpmath as mp

    t_absolute = mp.mpf(
        abs(t_stat)
    )

    df_t = mp.mpf(
        degrees_of_freedom
    )

    beta_argument = (
        df_t
        /
        (
            df_t
            +
            t_absolute ** 2
        )
    )

    p_value = float(
        mp.betainc(
            df_t / 2,
            mp.mpf("0.5"),
            0,
            beta_argument,
            regularized=True
        )
    )

except ImportError:

    raise ImportError(
        "The mpmath package is required for the "
        "p-value calculation. Install it with: "
        "python -m pip install mpmath"
    )


# 
# Displaying t-test results
# 

print("\n" + "=" * 70)
print("WELCH'S INDEPENDENT TWO-SAMPLE T-TEST")
print("=" * 70)

print(f"\nForward mean:          {forward_mean:.4f}")
print(f"Midfielder mean:       {midfielder_mean:.4f}")

print(f"\nForward sample size:    {forward_n}")
print(f"Midfielder sample size: {midfielder_n}")

print(f"\nt-statistic:            {t_stat:.4f}")
print(
    f"Degrees of freedom:    "
    f"{degrees_of_freedom:.2f}"
)
print(f"p-value:                {p_value:.6f}")


# 
# Statistical interpretation
# 

alpha = 0.05

print("\nSignificance level:", alpha)

if p_value < alpha:

    print(
        "\nResult: Reject the null hypothesis."
    )

    print(
        "There is statistically significant evidence "
        "of a difference in mean goals per game."
    )

else:

    print(
        "\nResult: Fail to reject the null hypothesis."
    )

    print(
        "There is not statistically significant evidence "
        "of a difference in mean goals per game."
    )


# 
# Answering the research question
# 

print("\n" + "=" * 70)
print("ANSWER TO RESEARCH QUESTION")
print("=" * 70)

if forward_mean > midfielder_mean:

    print(
        f"\nYes. Forwards scored more goals per game "
        f"on average ({forward_mean:.4f}) than "
        f"midfielders ({midfielder_mean:.4f})."
    )

else:

    print(
        f"\nNo. Forwards did not score more goals per game "
        f"on average ({forward_mean:.4f}) than "
        f"midfielders ({midfielder_mean:.4f})."
    )


# 
# Creating box plot
# 

plt.figure(figsize=(8, 6))

player_data.boxplot(
    column="goals_per_game",
    by="position"
)

plt.title(
    "Goals per Game by Player Position"
)

plt.suptitle("")

plt.xlabel("Player Position")

plt.ylabel("Goals per Game")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "task1_goals_per_game_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

# Closing the figure instead of displaying an additional
# blank Matplotlib window.
plt.close()


# 
# Saving cleaned player-level dataset
# 

player_data.to_csv(
    "task1_player_level_data.csv",
    index=False
)


# 
# Finalising
# 

print("\n" + "=" * 70)
print("FILES CREATED")
print("=" * 70)

print(
    "\nSaved cleaned player data:"
    "\ntask1_player_level_data.csv"
)

print(
    "\nSaved box plot:"
    "\ntask1_goals_per_game_boxplot.png"
)

print("\nAnalysis complete.")