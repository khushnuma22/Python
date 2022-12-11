Principal = int(input("Enter Principal :"))
Year = int(input("Enter Numbers of Year : "))
print("Principal Amount : RS. ", Principal)
print("Numbers of years : ", Year)
Rate = 5 if Year < 1 else 5.5 if Year <= 3 and Year > 1 else 6 if Year <= 5 and Year > 3 else 5.75
Simple_Interest = (Principal * Rate * Year) / 100
print("Simple Interest : RS.",Simple_Interest)
print("Maturity Amount : RS.", (Principal + Simple_Interest))