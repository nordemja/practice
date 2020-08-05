''' program that takes in a table name, pop, risk gives amount of tests to be sent there '''
import math

class covidTesting:
    def __init__(self, population, risk, tests):
        self.population = population
        self.risk = risk
        self.tests = tests

numCities = int(input("Enter number of cities to distribute test kits to: "))
tests = int(input("Enter amount of test kits available: "))
remainingTests = float(tests)

populationList = []
riskList = []

print('--------------------------------------------------')

x = 1
while x <= numCities:
    population = int(input("\nEnter population of city " + str(x) + " : "))
    risk = int(input("Enter risk factor (1-10): "))


    cityCovid = covidTesting(population, risk, tests)

    populationList.append(cityCovid.population)
    riskList.append(cityCovid.risk)

    x += 1

x = 1
for each in populationList:
    proportion = float(each/remainingTests) * 100
    testsNumToCity = float(remainingTests * (proportion/100))
    remainingTests = float(remainingTests - (remainingTests * (proportion/100)))
    print('\nCity ' + str(x) + " should receive " + str(round(proportion,2)) + " percent of remaining tests.")
    testsNumToCity = int(round(testsNumToCity, 0))
    print("For a total of: " + str(testsNumToCity) + " tests.")
    print("There are now: " + str(int(remainingTests)) + " remaining tests.")
    x += 1