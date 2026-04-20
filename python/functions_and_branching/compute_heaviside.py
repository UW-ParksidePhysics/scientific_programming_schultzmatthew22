def compute_heaviside(position):
    if position < 0:
        return 0
    else:
        return 1

def test_heaviside():
    test_values = [
        -10,
        -10 - 15,
        0,
        10 - 15,
        10
    ]

    print(f"{'Input':<10} | {'Result':<10}")
    print("-" * 23)

    for val in test_values:
        result = compute_heaviside(val)
        print(f"{val:<10} | {result:<10}")

if __name__ == "__main__":
    test_heaviside()