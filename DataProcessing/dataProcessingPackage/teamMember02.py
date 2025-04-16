# teamMember02.py
# Student Name: Zoha Iqbal
# email: iqbalza@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/16/25
# Course #/Section:  4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: Each team member completes one module that analyzes a shared car price dataset 
# and prints
# Brief Description of what this module does. This module processes car price data to calculate and display the average price by fuel type.
# Citations:N/A
# Anything else that's relevant:N/A

class teamMember02:
    def print_something_interesting(self, data):
        """
         Print the average car price for each fuel type.
        @param data list : the list of car records to process
        @return None
        """
        fuel_prices = {}
        fuel_counts = {}

        for row in data:
            fuel_type = row.get("fuel_type", "").strip()
            try:
                price = float(row.get("price", 0))
            except ValueError:
                continue 

            if fuel_type not in fuel_prices:
                fuel_prices[fuel_type] = 0
                fuel_counts[fuel_type] = 0

            fuel_prices[fuel_type] += price
            fuel_counts[fuel_type] += 1

        print("Team Member 02 - Average Price by Fuel Type:")
        for fuel, total_price in fuel_prices.items():
            avg_price = total_price / fuel_counts[fuel]
            print(f"  {fuel}: ${avg_price:,.2f}")

