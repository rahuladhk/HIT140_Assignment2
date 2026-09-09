import pandas as pd

df = pd.read_csv("wc2026_efi.csv")

#formatting data frame
discipline = df[
    [
        "player_id",
        "match_id",
        "team_id",
        "team_name",
        "player_name",
        "yellow_cards",
        "red_cards",
        "fouls_for",
        "fouls_against",
        "position"
    ]
]

#saving new csv file
discipline.to_csv("FIFA_2026_Discipline.csv", index=False)

print("Discipline CSV created successfully!")
print("Rows:", len(discipline))
print("Columns:", discipline.columns.tolist())