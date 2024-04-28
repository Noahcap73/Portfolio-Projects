import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv("NBA_Data_Analysis/nba_games.csv")

#Inspecting the first few rows of the NBA dataset
#print(tabulate(nba.head(), headers="keys"))

#Printing summary statistics for the data
#print(tabulate(nba.describe(), headers="keys"))

#Subsetting the data into two smaller datasets
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

#Comparing the points earned per game from the Knicks and Nets
knicks_pts_10 = nba_2010.pts[nba_2010.fran_id == "Knicks"]
nets_pts_10 = nba_2010.pts[nba_2010.fran_id == "Nets"]

#Calculating the average of points for both teams
knicks_pts_10_mean = knicks_pts_10.mean()
nets_pts_10_mean = nets_pts_10.mean()

#Calculating the difference between the two means
diff_means_2010 = knicks_pts_10_mean - nets_pts_10_mean
print(diff_means_2010) #Output: 9.73

#Creating overlapping histograms to compare the points scored
plt.hist(knicks_pts_10, color="steelblue", alpha = 0.7, density=True,  label="Knicks")
plt.hist(nets_pts_10, color="orange", alpha = 0.7, density=True, label="Nets")
plt.xlabel("Points")
plt.ylabel("Proportions of Games")
plt.legend()
plt.title("2010 Season")
plt.show()
plt.clf()

#Doing previous steps with the 2014 subset
knicks_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Knicks"]
nets_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Nets"]

knicks_pts_2014_mean = knicks_pts_2014.mean()
nets_pts_2014_mean = nets_pts_2014.mean()

diff_means_2014 = knicks_pts_10_mean - nets_pts_2014_mean
print(diff_means_2014) #Output: 3.97

plt.hist(knicks_pts_2014, color="steelblue", label="Knicks", density=True, alpha=0.7)
plt.hist(nets_pts_2014, color="Orange", density=True, alpha=0.7, label="Nets")
plt.xlabel("Points")
plt.ylabel("Proportions of Games")
plt.legend()
plt.show()
plt.clf()


#Visualizing the relationshops between franchise and points scored per game
sns.boxplot(data = nba_2010, x = "fran_id", y = "pts")
plt.legend()
plt.show()
plt.clf()

#Calculating a table of frequencies that shows the counts of game result and location
location_result_freq = pd.crosstab(nba_2010.game_location, nba_2010.game_result)
print(location_result_freq)

#Calculating the proportions for the table of frequencies
location_result_proportions = location_result_freq / len(location_result_freq)
print(location_result_proportions)

#Calculating the expected contingency table and the chi-square stastic
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

#Calculating covariance between forecast and point_diff
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff )
print(point_diff_forecast_cov)

#Calculating the correlation between forecat and point_diff
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

#Visualzing the correlation
plt.scatter(data=nba_2010, x = "forecast", y = "point_diff")
plt.legend()
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()


#Doing my own analysis
#Subsetting data to years 2010 - 2015
nba_2010_2015 = nba[(nba.year_id >= 2010) & (nba.year_id <= 2015) ]
#Filtering the data to only playoff games
nba_playoffs = nba_2010_2015[nba_2010_2015.is_playoffs == 1]

#Creating a function to find team fran_id statistics in playoffs
def team_statistics_fran(team_name):
    nba_playoffs_team = nba_playoffs[(nba_playoffs.fran_id == team_name)]
    nba_playoffs_games = len(nba_playoffs_team)
    nba_playoff_points = nba_playoffs_team.pts.mean()
    nba_playoff_opp_points = nba_playoffs_team.opp_pts.mean()
    nba_playoff_win_rate = len(nba_playoffs_team[nba_playoffs_team.game_result == "W"]) / len(nba_playoffs_team.game_result)
    return (f"Between 2010 - 2015, the {team_name} played in the playoffs {nba_playoffs_games} times. Had an average of {round(nba_playoff_points, 2)} points scored. Had an average of {round(nba_playoff_opp_points, 2)} points scored on them. And had a {round(100 * nba_playoff_win_rate, 2)}% win rate.")
    
#Creating a function to find team opp_fran statistics in playoffs
def team_statistics_opp(team_name):
    nba_playoffs_team = nba_playoffs[nba_playoffs.opp_fran == team_name]
    nba_playoffs_games = len(nba_playoffs_team)
    nba_playoff_points = nba_playoffs_team.opp_pts.mean()
    nba_playoff_fran_points = nba_playoffs_team.pts.mean()
    nba_playoff_win_rate = len(nba_playoffs_team[nba_playoffs_team.game_result == "L"]) / len(nba_playoffs_team.game_result)
    return (f"Between 2010 - 2015, the {team_name} played in the playoffs {nba_playoffs_games} times. Had an average of {round(nba_playoff_points, 2)} points scored. Had an average of {round(nba_playoff_fran_points, 2)} points scored on them. And had a {round(100 * nba_playoff_win_rate, 2)}% win rate.")
    






