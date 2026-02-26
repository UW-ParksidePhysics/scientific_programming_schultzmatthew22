one_billion_seconds = 1000000000
seconds_in_year = 60*60*24*365
billion_seconds_in_years = one_billion_seconds / seconds_in_year
cdc_life_expectancy_years = 79
years_can_live = cdc_life_expectancy_years >= billion_seconds_in_years
print(f"One billion seconds is {billion_seconds_in_years} years, the CDC life expectancy is {cdc_life_expectancy_years} years, so the answer is {'Yes' if years_can_live else 'No'}.")
