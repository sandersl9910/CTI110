gas_mileage = float(input())
cost_of_gas = float(input())

cost_per_mile = cost_of_gas / gas_mileage

twenty_miles = cost_per_mile * 20

seventyFive_miles = cost_per_mile * 75

fiveHundred_miles = cost_per_mile * 500

print(f'{twenty_miles:.2f} {seventyFive_miles:.2f} {fiveHundred_miles:.2f}')
