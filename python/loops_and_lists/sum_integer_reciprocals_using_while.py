summation = 0
starting_index = 1
index = starting_index
maximum_index = 3

while index <= maximum_index:
    summation += 1.0 / index
    index += 1

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:
    summation += 1.0 / index
    index += 1

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')


# index += 1 was missing and it created an infinite loop
# < was used instead of <= so it didn't include the last term
# using 1.0 instead of 1 looks cleaner? (idk)

# Hand calculations
# k=1: sum = 1/1 = 1.0
# k=2: sum = 1.0 + 1/2 = 1.5
# k=3: sum = 1.5 + 1/3 = 1.8333...


# --- LLM OUTPUT ---
# The script fails primarily due to an infinite loop; the loop counter 'index'
# is never incremented. Additionally, the loop terminates early because the
# '<' operator excludes the 'maximum_index' value. Adding 'index += 1' and
# changing the condition to '<=' resolves these issues.