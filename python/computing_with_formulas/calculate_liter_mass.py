densities = {
    "iron": 7.874,
    "air": 0.0012,
    "gasoline": 0.755,
    "ice": 0.9167,
    "human body": 1.10,
    "silver": 10.49,
    "platinum": 21.45
}

V=1000

print(f"{'Substance':10}\t{'Mass of 1L (g)':14}")
print("-"*35)
for substance, x in densities.items():
    mass = x * V
    print(f" {substance:10}\t{mass:14.4f}")
