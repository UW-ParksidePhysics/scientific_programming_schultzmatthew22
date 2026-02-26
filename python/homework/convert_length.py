km_from_college = 20.6
cm_per_km = 100000
cm_per_inch = 2.54
inches_per_foot = 12
feet_per_yard = 3
yards_per_mile = 1760

inches = (km_from_college * cm_per_km) / cm_per_inch
feet = inches / inches_per_foot
yards = feet / feet_per_yard
miles = yards / yards_per_mile

print(f"{km_from_college} km")
print(f"Inches: {inches}, Feet: {feet}, Yards: {yards}, Miles: {miles}")
print("-" * 30)

test_km = 0.640
test_inches = (test_km * cm_per_km) / cm_per_inch
test_feet = test_inches / inches_per_foot
test_yards = test_feet / feet_per_yard
test_miles = test_yards / yards_per_mile

print(f"{test_km} km")
print(f"{test_inches} inches")
print(f"{test_feet} feet")
print(f"{test_yards} yards")
print(f"{test_miles} miles")

