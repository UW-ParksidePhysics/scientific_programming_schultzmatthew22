maximum_integer = 100

loop_sum = 0

for i in range(1, maximum_integer + 1):
    loop_sum += i

formula_sum = (maximum_integer * (maximum_integer - 1)) / 2

print (f"n = {maximum_integer}")
print(f"sum(1, n) = {loop_sum}")
print(f"n(n+1)/2 = {int(loop_sum)}")