
# --- Variables ---
name = "Haseeb"
age = 26
drinks_coffee = False
salary = 7500000.0

# --- Formatted sentence ---
print(f"Hi, I'm {name}, I'm {age} years old, my salary is Rs. {salary:,.2f}, and I {'do' if drinks_coffee else 'do not'} drink coffee.")

# --- Years until retirement ---
retirement_age = 60
years_to_retirement = retirement_age - age
print(f"Years until retirement: {years_to_retirement}")

# --- Weekly coffee budget ---
cups_per_day = 3
cost_per_cup = 150
days_in_week = 7
weekly_coffee_budget = cups_per_day * cost_per_cup * days_in_week

if drinks_coffee:
    print(f"Weekly coffee budget: Rs. {weekly_coffee_budget}")
else:
    print("I dont drink coffee. Lets save money.")
