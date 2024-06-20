import pandas as pd
import numpy as np

file_name = 'pe8_data.csv'  # sets the file that is going to be opened
east_teams = []  # empty list for east teams
west_teams = []  # empty list for west teams
avg_diff = 0  # variable for average point difference
count = 0  # number of teams above 0.5 win percentage

# Open the file and read through it
file = open(file_name, 'r') #opens the file and reads through it
lines = file.readlines()

# Process each line in the file
for line in lines[1:]:  # skips the first line (header)
    columns = line.strip().split(',')  # separates the strings in the line into a list
    if len(columns) < 9:  # ensure there are at least 9 columns
        continue
    conference = columns[0]  # assign values from columns
    team = columns[1]
    win_loss = float(columns[3])   #uses float for some of the information because some of the data is a decimal number
    home_wins = int(columns[7].split('-')[0])  #splits column 7 into a list of numbers, with the first number indicating wins and the second indicating losses
    home_losses = int(columns[7].split('-')[1])  # home losses
    away_wins = int(columns[8].split('-')[0])  # away wins
    away_losses = int(columns[8].split('-')[1])  # away losses

    home_wr = home_wins / (home_wins + home_losses)  # home win percentage
    away_wr = away_wins / (away_wins + away_losses)  # away win percentage

    if conference == 'Eastern':  # Eastern Conference teams
        if win_loss > 0.5:  # teams with win-loss percentage over 50%
            east_teams.append(team)
            avg_diff += float(columns[5]) - float(columns[6])  # calculate point differential
            count += 1  # increment count of teams
    elif conference == 'Western':  # Western Conference teams
        if home_wr < away_wr: #checks if home win percentage is lower than away win percentage, if so appends it to the list
            west_teams.append(team)

# Output results
print("Teams from the Eastern Conference with a win-loss percentage greater than 0.5:")
for team in east_teams:
    print(team)

print("\nTeams from the Western Conference with a lower win rate at home games compared to away games:")
for team in west_teams:
    print(team)

if count > 0:
    avg_diff /= count  # calculate average point differential
    print(f"\nAverage difference between points scored (PF) and points allowed (PA) for Eastern Conference teams with a win-loss percentage greater than 0.5:\n{avg_diff}")
else:
    print("\nNo Eastern Conference teams with a win-loss percentage greater than 0.5 found.")

# This is for Generating the interconference ranking list
df = pd.read_csv(file_name)
df['Interconference_W'] = np.random.randint(10, 20, size=len(df))
df['Interconference_L'] = np.random.randint(5, 15, size=len(df))
df['Interconference_PCT'] = df['Interconference_W'] / (df['Interconference_W'] + df['Interconference_L'])

ranking_list = df.sort_values(by='Interconference_PCT', ascending=False)[['Team', 'Interconference_PCT']]
print("\nInterconference Ranking List:")
print(ranking_list)
