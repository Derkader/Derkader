"""
Created on July 9, 2022

@author: derek nash

Save to Classes Assignment
"""
import csv
import re


class County:

    def __init__(self, county_name, per_cap_income, med_house_income, med_family_income, population, num_households):
        self.county_name = county_name
        self.per_cap_income = per_cap_income
        self.med_house_income = med_house_income
        self.med_family_income = med_family_income
        self.population = population
        self.num_households = num_households

    def display_households(self):
        return self.num_households

    def display_population(self):
        return self.population

    def __str__(self):
        return 'This is ' + str(self.county_name) + ' County'


with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_pop = 0
    # initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue

        if row[1] != 'United States' and row[1] != 'Iowa State':  # skip these rows
            county[str(row[1])] = County(row[1], row[2], row[3], row[4], row[5], row[
                6])  # create an item in dictionary county with a key of the county name and a value of the object
            total_pop += int(re.sub(",", "", row[5]))

    csv_file.close()

temp_county = county['Dallas']
print(str(temp_county))
print('Population: ' + str(temp_county.display_population()))
print('Households: ' + str(temp_county.display_households()))
print()
print('Total population of Iowa is ' + str(total_pop))
