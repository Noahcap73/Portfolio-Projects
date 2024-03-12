import pandas as pd
from tabulate import tabulate

visits = pd.read_csv('Merging_pandas/visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('Merging_pandas/cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('Merging_pandas/checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('Merging_pandas/purchase.csv',
                       parse_dates=[1])

print(tabulate(visits.head()))
print(tabulate(cart.head()))
print(tabulate(checkout.head()))
print(tabulate(purchase.head()))

#Left merging visits and carts
visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart)

#Finding how long the merged DataFrame is
print(len(visits_cart)) #2000 rows

#Finding how many of the timestamps are null for the column cart_time
cart_time_null = visits_cart[visits_cart["cart_time"].isnull()]
print(len(cart_time_null)) #1652

#Finding the percent of users who did not put a shirt in their cart
percent_of_cart_null = float(len(cart_time_null)) / float(len(visits_cart))
print(f"The percent of users who visited and didnt place a t-shirt in their cart is {percent_of_cart_null * 100}%") #82.6%

cart_checkout = pd.merge(cart, checkout, how="left")
#print(cart_checkout)

checkout_null = cart_checkout[cart_checkout["checkout_time"].isnull()]
#print(checkout_null)

#Finding the percentage of users who had items but didn't checkout
percent_of_checkout_null = float(len(checkout_null)) / float(len(cart_checkout))
print(f"The percentage of users who had items in their cart, but did not checkout is {percent_of_checkout_null * 100}%") #25.3%

#Merging all four DataFrames
all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")

print(tabulate(all_data, headers="keys", tablefmt="grid"))

#Finding how many users proceeded to checkout
amt_of_checkouts = all_data[all_data["checkout_time"].notnull()]

#Finding how many users did not pruchase a t-shirt
amt_of_null_purchases = all_data[all_data["purchase_time"].isnull()]

#Finding the percent of users who went to checkout but didn't purchase
percent_of_checkout_no_purchase = float(len(amt_of_checkouts["checkout_time"])) / float(len(amt_of_null_purchases["purchase_time"])) 

print(f"The percentage of users who proceeded to checkout, but did not purchase a t-shirt is {percent_of_checkout_no_purchase * 100}%") #31.8%

#Creating a column to find the average time from initial visit to final purchase
all_data["visit_to_purchase"] = all_data["purchase_time"] - all_data["visit_time"]
print(f'The average time to purchase is about {all_data["visit_to_purchase"].mean()}') #43.5 minutes