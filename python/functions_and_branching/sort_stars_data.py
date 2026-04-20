nearby_star_data = [
    ('Alpha Centauri A', 4.3, 0.26, 1.56),
    ('Alpha Centauri B', 4.3, 0.077, 0.45),
    ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
    ("Barnard's Star", 6.0, 0.00004, 0.0005),
    ('Wolf 359', 7.7, 0.00001, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('Luyten 726-8 A', 8.4, 0.00003, 0.00006),
    ('Luyten 726-8 B', 8.4, 0.00002, 0.00004),
    ('Sirius A', 8.6, 1.00, 23.6),
    ('Sirius B', 8.6, 0.001, 0.003),
    ('Ross 154', 9.4, 0.00002, 0.0005),
]

def print_table(title, data, index):
    print(f"\n--- Sorted by {title} ---")
    print(f"{'Star Name':<20} | {title:<18}")
    print("-" * 42)

    sorted_data = sorted(data, key=lambda x: x[index])

    for star in sorted_data:
        print(f"{star[0]:<20} | {star[index]:<18}")

print_table("Distance (ly)", nearby_star_data, 1)

print_table("Apparent Brightness", nearby_star_data, 2)

print_table("Luminosity", nearby_star_data, 3)