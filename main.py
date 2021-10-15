age = input("Enter your current Age:-")
age_as_int = int(age)

rem_years = 90 - age_as_int
rem_days = rem_years * 365
rem_weeks = rem_years * 52
rem_months = rem_years * 12

print(f"you have {rem_days} days,{rem_weeks} weeks,{rem_months} months")
