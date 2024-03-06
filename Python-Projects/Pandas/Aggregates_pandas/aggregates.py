import pandas as pd
from tabulate import tabulate

ad_clicks = pd.read_csv('aggregates_pandas/ad_clicks.csv')

#Examining the first few rows
print(tabulate(ad_clicks.head()))

#Finding how many views came from each utm_source
utm_source_views = ad_clicks.groupby("utm_source").count().reset_index()

#print(utm_source_views)

#Creating a column which is True if ad_click_timestamp is not null and False otherwise
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(tabulate(ad_clicks, headers="keys", tablefmt="grid"))

#Grouping utm_source and is_click and counting the user_id's on each group
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
print(tabulate(clicks_by_source, headers="keys", tablefmt="grid"))

#Pivoting the clicks_by_source data
clicks_pivot = clicks_by_source.pivot(
  columns="is_click",
  index="utm_source",
  values="user_id"
)

#Creating a column in clicks_pivot that is equal to the percent of users who clicked on the ad from each utm_source
clicks_pivot["percent_clicked"] = clicks_pivot[True] / \
  (clicks_pivot[True] + clicks_pivot[False])

#Finding if the same number of people were shown both ads
num_of_A_and_B = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(tabulate(num_of_A_and_B, headers="keys", tablefmt="grid"))

#Checking to see if a greater number of users clicked on ad A or B
A_or_B_clicks = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()

A_or_B_pivot = A_or_B_clicks.pivot(
  index="experimental_group",
  columns="is_click",
  values="user_id"
)

print(tabulate(A_or_B_pivot, headers="keys", tablefmt="grid"))

#Creating two DataFrames that contain the results of A and B group
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

print(tabulate(a_clicks, headers="keys", tablefmt="grid"))
print(tabulate(b_clicks, headers="keys", tablefmt="grid"))

#Creating a pivot table and calculating the percent of users who clocked on the ad by day for each group
a_clicks_pivot = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index().pivot(
  columns="is_click",
  index="day",
  values="user_id"
)\
.reset_index()

a_clicks_pivot["percent_clicked"] = a_clicks_pivot[True] / \
(a_clicks_pivot[True] + a_clicks_pivot[False])
print(tabulate(a_clicks_pivot, headers="keys", tablefmt="grid"))

b_clicks_pivot = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index().pivot(
  columns="is_click",
  index="day",
  values="user_id"
)\
.reset_index()

b_clicks_pivot["percent_clicked"] = b_clicks_pivot[True] / \
(b_clicks_pivot[True] + b_clicks_pivot[False])
print(tabulate(b_clicks_pivot, headers="keys", tablefmt="grid"))

#Ad A was better because it had a greater percent clicked for most of the days