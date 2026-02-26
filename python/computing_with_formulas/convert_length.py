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

print(f"Distance from campus: {km_from_college} km")
print(f"Inches: {inches:.3f}, Feet: {feet:.3f}, Yards: {yards:.3f}, Miles: {miles:.3f}")
print("-" * 30)

test_km = 0.640
test_inches = (test_km * cm_per_km) / cm_per_inch
test_feet = test_inches / inches_per_foot
test_yards = test_feet / feet_per_yard
test_miles = test_yards / yards_per_mile

print(f"Test Distance: {test_km} km")
print(f"Inches: {test_inches:.3f} inches, "
      f"Feet: {test_feet:.3f} feet, "
      f"Yards: {test_yards:.3f} yards, "
      f"Miles: {test_miles:.3f} miles")

