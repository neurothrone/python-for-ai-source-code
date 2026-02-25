# Principal amount - 100 000 SEK
# Annual interest rate - 1.6 %
# Time Period - 90 days
# Capital tax = 30 %

# Interest = 100 000 * (90 / 365) * 0.016 * 0.7
#print(100_000 * (90 / 365) * 0.016 * 0.7)

# Improve Readability
#principal_amount = 100_000
#interest_rate = 0.016
#time_period = 90
#year_days = 365
#capital_tax = 0.3

#profit_amount = principal_amount * (time_period / year_days) * interest_rate * (1.0 - capital_tax)
#print(f"For {principal_amount} SEK saved for {time_period} days, you will profit after tax about {profit_amount:.2f} SEK.")

# Improve Usability
principal_amount = int(input("Enter principal amount in SEK: "))
interest_rate = float(input("Enter annual interest rate (format: 0.016): "))
time_period = int(input("Enter time period in days (for example 90): "))
year_days = 365
capital_tax = float(input("Enter capital tax (example: 0.3): "))

profit_amount = principal_amount * (time_period / year_days) * interest_rate * (1.0 - capital_tax)
print(f"For {principal_amount} SEK saved for {time_period} days, you will profit after tax about {profit_amount:.2f} SEK.")