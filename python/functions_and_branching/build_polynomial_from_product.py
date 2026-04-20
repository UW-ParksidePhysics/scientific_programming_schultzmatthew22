def construct_polynomial_from_roots(x, roots):
    p_x = 1

    for r in roots:
        p_x *= (x - r)

    return p_x

test_roots = [1, 2, 3]
test_x = 4
result = construct_polynomial_from_roots(test_x, test_roots)

print(f"Roots: {test_roots}")
print(f"Evaluating at x = {test_x}")
print(f"p({test_x}) = {result}")

if result == 6:
    print("Test Successful")
else:
    print("Test Not Successful.")