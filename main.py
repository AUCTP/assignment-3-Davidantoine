
# 1. Simulate Daily Demand and Analyze Results
# Write a function that simulates the daily demand for the product over the next n days using a Poisson distribution.

# Steps:

# Assume the average daily demand (λ) is 20 units.
# Use numpy to generate Poisson-distributed daily demand for n days.
# Analyze the Results:

# Calculate and print the following statistics from the simulation results:
# Mean (average) daily demand
# Standard deviation
# 5th percentile (to understand the lower bound in a worst-case scenario)
# 95th percentile (to understand the upper bound in a best-case scenario)
# Interpret the results in the context of inventory management.

import numpy as np


def demand_n_days(n, avg_demand):
    demand = []
    for i in range(n):
        daily_demand = np.random.poisson(avg_demand)
        demand.append(daily_demand)
    return demand

def demand_stats(demand):
    mean_demand = np.mean(demand)
    std_demand = np.std(demand)
    perc_5 = np.percentile(demand, 5)
    perc_95 = np.percentile(demand, 95)

    print(f"Mean Demand: {mean_demand}")
    print(f"Standard Deviation: {std_demand}")
    print(f"5th Percentile: {perc_5}")
    print(f"95th Percentile: {perc_95}")

def demand_sim1000():
    demand_simulations = []
    for i in range(10000):
        demandX = demand_n_days(n, avg_demand)
        monthdemand = sum(demandX)
        demand_simulations.append(monthdemand)
    return demand_simulations



#*** Main program***
n = 30 
avg_demand = int(input("Enter the average daily demand: "))
service_level = int(input("Enter the service level (as a percentage): "))
demand = demand_n_days(n, avg_demand)
demand_stats(demand_sim1000())

optimal_inventory = np.percentile(demand_sim1000(), service_level)
print(f"Optimal Inventory Level to maintain service level {service_level}%: {np.ceil(optimal_inventory):0.0f} units")







