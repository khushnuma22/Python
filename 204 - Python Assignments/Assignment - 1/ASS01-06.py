Principal = int(input("Enter Principal :"))
Year = int(input("Enter Numbers of Year : "))
print("Principal Amount : RS. ", Principal)
print("Numbers of years : ", Year)
if Year > 1:
    if 1 <= Year and Year < 3:
        Rate = 5.5
    elif 3 <= Year and Year < 5:
        Rate = 6
    else:
        Rate = 5.75
else:
    Rate = 5
Simple_Interest = (Principal * Rate * Year) / 100
print("Simple Interest : RS.",Simple_Interest)
print("Maturity Amount : RS.", (Principal + Simple_Interest))