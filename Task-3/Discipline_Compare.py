import pandas as pd

# LOAD DATA

df = pd.read_csv("FIFA_2026_Discipline.csv")

# SELECT REQUIRED COLUMNS

loaded = df[
    [
        "match_id",
        "player_id",
        "player_name",
        "position",
        "yellow_cards",
        "red_cards"
    ]
]


# KEEP ONLY DEFENDERS AND FORWARDS

loaded_df2 = loaded[
    loaded["position"].isin(["Defender", "Forward"])
].copy()


# REMOVE PLAYERS WITH NO CARDS

loaded_df3 = loaded_df2[
    (loaded_df2["yellow_cards"] > 0) |
    (loaded_df2["red_cards"] > 0)
].copy()


# GET EVERY MATCH

matches = loaded["match_id"].unique()


# COMPARE EVERY MATCH

results = []

for match_id in matches:

    # Get players from this match
    match = loaded_df3[
        loaded_df3["match_id"] == match_id
    ]

    # Total yellow cards for each position
    yellow_cards = (
        match
        .groupby("position")["yellow_cards"]
        .sum()
    )

    defender_yellow = yellow_cards.get("Defender", 0)
    forward_yellow = yellow_cards.get("Forward", 0)


    # Determine winner
    if defender_yellow > forward_yellow:
        result = "Defender"
    elif forward_yellow > defender_yellow:
        result = "Forward"
    else:
        result = "Equal"


    # Store result
    results.append({
        "match_id": match_id,
        "defender_yellow_cards": defender_yellow,
        "forward_yellow_cards": forward_yellow,
        "result": result
    })


# CREATE RESULTS DATAFRAME

comparison = pd.DataFrame(results)


# DISPLAY RESULTS

print("\n==========================================")
print("YELLOW CARD COMPARISON FOR EVERY MATCH")
print("==========================================")

print(comparison.to_string(index=False))

#Count Number of cards and Compare

defender_cards = 0
forward_cards = 0

for index, row in loaded_df2.iterrows():

    yellow = row["yellow_cards"]

    if pd.isna(yellow):
        yellow = 0

    if row["position"] == "Defender":
        defender_cards += yellow

    elif row["position"] == "Forward":
        forward_cards += yellow


print("Total Defender yellow cards:", defender_cards)
print("Total Forward yellow cards:", forward_cards)

if defender_cards > forward_cards:
    print("Result: Defenders got more yellow cards.")

elif forward_cards > defender_cards:
    print("Result: Forwards got more yellow cards.")

else:
    print("Result: Both got the same number of yellow cards.")